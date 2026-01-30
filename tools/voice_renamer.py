"""
Voice Renamer - Renomeia arquivos de áudio para os IDs do Auto Voice
Extrai diálogos dos scripts .rpy, normaliza, faz match com os arquivos de áudio
e renomeia para os IDs do dialogue.tab, organizando por cenas.
"""
import os
import re
import shutil
from pathlib import Path
from difflib import SequenceMatcher

# Diretórios
PROJECT_DIR = Path(__file__).parent.parent
SCENES_DIR = PROJECT_DIR / "game" / "scenes"
DIALOGUE_TAB = PROJECT_DIR / "dialogue.tab"
# Diretório onde estão os arquivos de áudio originais/fatiados
# Ajuste este caminho para onde seus áudios estão localizados
AUDIO_SOURCE = Path(r"C:\Caminho\Para\Seus\Audios")
VOICE_OUTPUT = PROJECT_DIR / "game" / "voice"

MIN_SCORE = 0.6

CHARACTERS = ["michael", "darryl", "pam", "kevin", "philys", 
              "jim", "karen", "creed", "jan", "toby", 
              "stanley", "hunter"]

DIALOGUE_PATTERN = re.compile(r'^(\s*)(\w+)\s+"(.+)"', re.MULTILINE)


def normalize_text(text):
    """Normaliza texto para o formato dos arquivos de áudio"""
    text = re.sub(r'[^\w\s]', '', text.lower())
    text = re.sub(r'\s+', '_', text.strip())
    return text


def extract_audio_text(filename):
    """Extrai o texto do nome do arquivo de áudio (remove número e extensão)"""
    name = Path(filename).stem
    name = re.sub(r'^\d+_', '', name)
    return name


def similarity(a, b):
    """Retorna score de similaridade entre 0 e 1"""
    return SequenceMatcher(None, a, b).ratio()


def extract_dialogues_from_scene(filepath):
    """Extrai diálogos de um arquivo .rpy com texto normalizado"""
    dialogues = []
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = DIALOGUE_PATTERN.findall(content)
    
    for indent, character, text in matches:
        char_lower = character.lower()
        if char_lower in CHARACTERS:
            normalized = normalize_text(text)
            dialogues.append({
                'character': char_lower,
                'original': text,
                'normalized': normalized
            })
    
    return dialogues


def load_dialogue_tab():
    """Carrega o dialogue.tab e retorna lista de diálogos com IDs"""
    dialogues = []
    with open(DIALOGUE_TAB, 'r', encoding='utf-8') as f:
        next(f)  # Pula header
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                dialogues.append({
                    'id': parts[0],
                    'character': parts[1],
                    'text': parts[2],
                    'normalized': normalize_text(parts[2])
                })
    return dialogues


def find_best_audio_match(dialogue_normalized, audio_files):
    """Encontra o melhor arquivo de áudio para um diálogo"""
    best_audio = None
    best_score = 0
    
    for audio_file in audio_files:
        audio_text = extract_audio_text(audio_file.name)
        score = similarity(dialogue_normalized, audio_text)
        
        if score > best_score:
            best_score = score
            best_audio = audio_file
    
    return best_audio, best_score


def main():
    print("=" * 60)
    print("VOICE RENAMER - Renomeia áudios para IDs do Auto Voice")
    print("=" * 60)
    
    # Carregar dialogue.tab para obter os IDs
    dialogue_tab = load_dialogue_tab()
    print(f"Carregados {len(dialogue_tab)} diálogos do dialogue.tab")
    
    # Criar índice de diálogos por texto normalizado
    dialogue_by_normalized = {}
    for d in dialogue_tab:
        if d['normalized'] not in dialogue_by_normalized:
            dialogue_by_normalized[d['normalized']] = d
    
    # Listar todos os arquivos de áudio
    audio_files = list(AUDIO_SOURCE.glob("*.mp3")) + list(AUDIO_SOURCE.glob("*.ogg"))
    print(f"Encontrados {len(audio_files)} arquivos de áudio")
    
    # Processar cada cena
    scene_files = sorted(SCENES_DIR.glob("scene_*.rpy"))
    
    total_matched = 0
    total_missing = 0
    
    for scene_file in scene_files:
        scene_name = scene_file.stem  # ex: scene_1_michael_office
        print(f"\n--- Processando {scene_name} ---")
        
        # Criar pasta da cena
        scene_output = VOICE_OUTPUT / scene_name
        scene_output.mkdir(parents=True, exist_ok=True)
        
        # Extrair diálogos da cena
        dialogues = extract_dialogues_from_scene(scene_file)
        
        matched = 0
        missing = 0
        
        for idx, dialogue in enumerate(dialogues, 1):
            # Encontrar o ID no dialogue.tab
            dialogue_id = None
            if dialogue['normalized'] in dialogue_by_normalized:
                dialogue_id = dialogue_by_normalized[dialogue['normalized']]['id']
            
            # Encontrar arquivo de áudio correspondente
            best_audio, score = find_best_audio_match(dialogue['normalized'], audio_files)
            
            if best_audio and score >= MIN_SCORE and dialogue_id:
                # Copiar e renomear para o ID
                ext = best_audio.suffix
                new_name = f"{dialogue_id}{ext}"
                dest = scene_output / new_name
                
                shutil.copy(str(best_audio), str(dest))
                print(f"  ✓ {idx:03d}: {dialogue_id} (score: {score:.2f})")
                matched += 1
            else:
                # Marcar como faltando
                reason = "sem áudio" if score < MIN_SCORE else "sem ID"
                print(f"  ✗ {idx:03d}: {dialogue['normalized'][:40]}... [{reason}]")
                missing += 1
        
        print(f"  Resultado: {matched} ok, {missing} faltando")
        total_matched += matched
        total_missing += missing
    
    print(f"\n{'='*60}")
    print(f"TOTAL: {total_matched} arquivos copiados, {total_missing} faltando")
    print(f"Saída: {VOICE_OUTPUT}")


if __name__ == "__main__":
    main()
