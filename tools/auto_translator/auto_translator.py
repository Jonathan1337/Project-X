import os
import re
import sys
import time
import requests
from pathlib import Path

# Configurar encoding UTF-8 para output no Windows
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Configuração do Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "gemma3:4b"  # Modelo instalado localmente

def parse_renpy_translation_file(filepath):
    """Extrai os blocos de tradução do arquivo.rpy"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def find_empty_translations(content):
    """Encontra todas as linhas que precisam de tradução.
    
    Suporta três formatos:
    1. old "texto" / new "" (usado em common.rpy, screens.rpy)
    2. # personagem "texto" / personagem "" (diálogos com personagem)
    3. # "texto" / "" (narrações sem personagem)
    """
    matches = []
    
    # Padrão 1: old "texto" seguido de new ""
    pattern_old_new = r'(old\s+"([^"]*)")\s*\n(\s*)(new\s+"")'
    for match in re.finditer(pattern_old_new, content):
        matches.append({
            'type': 'old_new',
            'match': match,
            'original_text': match.group(2),
            'indent': match.group(3),
            'full_match': match.group(0),
            'start': match.start(),
            'end': match.end()
        })
    
    # Padrão 2: # personagem "texto" seguido de personagem ""
    # Formato: # character "text" \n    character ""
    pattern_dialogue = r'(#\s*(\w+)\s+"([^"]*)")\s*\n(\s*)(\2\s+"")'
    for match in re.finditer(pattern_dialogue, content):
        original_text = match.group(3)
        if original_text.strip():  # Ignora textos vazios
            matches.append({
                'type': 'dialogue',
                'match': match,
                'original_text': original_text,
                'character': match.group(2),
                'indent': match.group(4),
                'full_match': match.group(0),
                'start': match.start(),
                'end': match.end()
            })
    
    # Padrão 3: # "texto" seguido de "" (narração sem personagem)
    # Formato: # "text" \n    ""
    pattern_narration = r'(#\s+"([^"]*)")\s*\n(\s*)("")'
    for match in re.finditer(pattern_narration, content):
        original_text = match.group(2)
        if original_text.strip():  # Ignora textos vazios
            matches.append({
                'type': 'narration',
                'match': match,
                'original_text': original_text,
                'character': '',
                'indent': match.group(3),
                'full_match': match.group(0),
                'start': match.start(),
                'end': match.end()
            })
    
    # Ordenar por posição no arquivo (decrescente para processar de trás para frente)
    matches.sort(key=lambda x: x['start'], reverse=True)
    
    return matches

def translate_text(text, target_lang='pt-BR'):
    """Traduz texto usando Ollama local"""
    if not text or not text.strip():
        return ""
    
    try:
        prompt = f"""Translate the following text from English to Brazilian Portuguese (pt-BR).
Keep the original tone and style. Return ONLY the translation, nothing else.
If there are special Ren'Py markups like {{{{...}}}} or [[...]], keep them intact.

Text: {text}

Translation:"""
        
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,  # Mais determinístico para traduções
                    "num_predict": 500   # Limite de tokens na resposta
                }
            },
            timeout=60
        )
        
        if response.status_code == 200:
            result = response.json()
            translated = result.get("response", "").strip()
            
            # Remove aspas extras se o modelo adicionar
            if translated.startswith('"') and translated.endswith('"'):
                translated = translated[1:-1]
            
            # Remove prefixos comuns que o modelo pode adicionar
            prefixes_to_remove = ["Translation:", "Tradução:", "Portuguese:"]
            for prefix in prefixes_to_remove:
                if translated.lower().startswith(prefix.lower()):
                    translated = translated[len(prefix):].strip()
            
            return translated
        else:
            print(f"  Erro HTTP {response.status_code}: {response.text}")
            return None
    
    except requests.exceptions.ConnectionError:
        print("  Erro: Ollama não está rodando. Execute 'ollama serve' primeiro.")
        return None
    except Exception as e:
        print(f"  Erro ao traduzir: {e}")
        return None

def translate_file(filepath, dry_run=False):
    """Traduz um arquivo .rpy substituindo traduções vazias pelo texto traduzido"""
    print(f"\n{'='*60}")
    print(f"Processando: {filepath}")
    print(f"{'='*60}")
    
    content = parse_renpy_translation_file(filepath)
    matches = find_empty_translations(content)
    
    if not matches:
        print("  Nenhuma tradução pendente encontrada.")
        return 0
    
    print(f"  Encontradas {len(matches)} linhas para traduzir.")
    
    translations_made = 0
    new_content = content
    
    # matches já está ordenado de trás para frente
    for m in matches:
        old_text = m['original_text']
        indent = m['indent']
        
        if not old_text.strip():
            continue
            
        print(f"\n  Original: \"{old_text[:60]}{'...' if len(old_text) > 60 else ''}\"")
        
        translated = translate_text(old_text)
        
        if translated:
            # Sanitizar a tradução: converter quebras de linha reais para \n
            translated = translated.replace('\r\n', '\\n').replace('\r', '\\n').replace('\n', '\\n')
            # Escapar aspas internas
            translated = translated.replace('"', '\\"')
            
            print(f"  Tradução: \"{translated[:60]}{'...' if len(translated) > 60 else ''}\"")
            
            # Gerar substituição baseada no tipo
            match_obj = m['match']
            if m['type'] == 'old_new':
                # Formato: old "texto" \n    new "tradução"
                new_block = f'{match_obj.group(1)}\n{indent}new "{translated}"'
            else:
                # Formato dialogue: # character "texto" \n    character "tradução"
                character = m['character']
                comment_line = match_obj.group(1)
                if character:
                    new_block = f'{comment_line}\n{indent}{character} "{translated}"'
                else:
                    new_block = f'{comment_line}\n{indent}"{translated}"'
            
            new_content = new_content[:m['start']] + new_block + new_content[m['end']:]
            
            translations_made += 1
        else:
            print(f"  [!] Falha na tradução, mantendo vazio.")
    
    if not dry_run and translations_made > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"\n[OK] Arquivo salvo com {translations_made} traduções.")
    elif dry_run:
        print(f"\n[DRY RUN] {translations_made} traduções seriam aplicadas.")
    
    return translations_made

def check_ollama_running():
    """Verifica se o Ollama está rodando"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return response.status_code == 200
    except:
        return False

def process_translation_files(input_dir, target_lang='pt-BR', dry_run=False):
    """Processa todos os arquivos .rpy no diretório"""
    
    # Verifica se Ollama está rodando
    if not check_ollama_running():
        print("[ERRO] Ollama não está rodando!")
        print("   Execute 'ollama serve' em outro terminal e tente novamente.")
        return
    
    print(f"[OK] Ollama conectado! Usando modelo: {OLLAMA_MODEL}")
    
    input_path = Path(input_dir)
    
    if not input_path.exists():
        print(f"Erro: Diretório não encontrado: {input_dir}")
        return
    
    rpy_files = list(input_path.glob('**/*.rpy'))
    
    if not rpy_files:
        print(f"Nenhum arquivo .rpy encontrado em: {input_dir}")
        return
    
    print(f"\nEncontrados {len(rpy_files)} arquivos .rpy")
    print(f"Modo: {'DRY RUN (simulação)' if dry_run else 'TRADUÇÃO REAL'}")
    
    total_translations = 0
    
    for rpy_file in rpy_files:
        translations = translate_file(rpy_file, dry_run=dry_run)
        total_translations += translations
    
    print(f"\n{'='*60}")
    print(f"RESUMO: {total_translations} traduções realizadas em {len(rpy_files)} arquivos.")
    print(f"{'='*60}")

# Uso
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Traduz arquivos Ren\'Py automaticamente usando Ollama')
    parser.add_argument('--input', '-i', default='game/tl/portuguese',
                        help='Diretório com arquivos .rpy para traduzir')
    parser.add_argument('--dry-run', '-d', action='store_true',
                        help='Simula tradução sem salvar arquivos')
    parser.add_argument('--lang', '-l', default='pt-BR',
                        help='Idioma de destino (padrão: pt-BR)')
    parser.add_argument('--model', '-m', default='gemma3:4b',
                        help='Modelo Ollama a usar (padrão: gemma3:4b)')
    
    args = parser.parse_args()
    
    # Atualiza modelo se especificado
    if args.model:
        OLLAMA_MODEL = args.model
    
    process_translation_files(
        input_dir=args.input,
        target_lang=args.lang,
        dry_run=args.dry_run
    )