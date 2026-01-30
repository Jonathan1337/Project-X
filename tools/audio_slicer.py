import re
from pathlib import Path
from pydub import AudioSegment

#função para converter timecode em ms

def timecode_to_ms(timecode):

    timecode = timecode.replace(',','.')

    partes = timecode.split(':')
    horas = int(partes[0])
    minutos = int(partes[1])
    segundos = float(partes[2])

    total_ms = (horas * 3600 + minutos * 60 + segundos) * 1000

    return int(total_ms)

#função para limpar texto e gerar nome de arquivo

def criar_nome_arquivo(indice, texto):

    texto_limpo = re.sub(r'[^\w\s]', '', texto, flags=re.UNICODE)

    palavras = texto_limpo.split()
    
    # Junta com underscore e converte para minúsculo
    nome = '_'.join(palavras).lower()
    
    # Formata: 001_texto_aqui.mp3
    return f"{indice:03d}_{nome}.mp3"


# Função para fazer o parse do arquivo SRT

def parse_srt(caminho_srt):
    # Lista para guardar as legendas
    legendas = []
    
    # Lê o arquivo
    with open(caminho_srt, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    # Divide em blocos (separados por linha em branco)
    blocos = conteudo.strip().split('\n\n')
    
    for bloco in blocos:
        linhas = bloco.strip().split('\n')
        
        if len(linhas) >= 3:
            # Linha 1: índice (ignoramos)
            # Linha 2: timecodes
            # Linha 3+: texto
            
            timecode_linha = linhas[1]
            texto = ' '.join(linhas[2:])  # Junta todas as linhas de texto
            
            # Extrai início e fim: "00:00:01,500 --> 00:00:04,000"
            partes = timecode_linha.split(' --> ')
            inicio = partes[0].strip()
            fim = partes[1].strip()
            
            legendas.append({
                'inicio': inicio,
                'fim': fim,
                'inicio_ms': timecode_to_ms(inicio),
                'fim_ms': timecode_to_ms(fim),
                'texto': texto
            })
    
    return legendas

def slice_audio(caminho_audio, caminho_srt, pasta_saida):
    # Cria a pasta de saída se não existir
    Path(pasta_saida).mkdir(parents=True, exist_ok=True)
    
    # Carrega o áudio
    print(f"Carregando áudio: {caminho_audio}")
    audio = AudioSegment.from_file(caminho_audio)
    
    # Faz o parse do SRT
    print(f"Lendo legendas: {caminho_srt}")
    legendas = parse_srt(caminho_srt)
    
    print(f"Encontradas {len(legendas)} legendas")
    
    # Para cada legenda, fatia e salva
    for i, legenda in enumerate(legendas, start=1):
        # Fatia o áudio
        trecho = audio[legenda['inicio_ms']:legenda['fim_ms']]
        
        # Gera o nome do arquivo
        nome_arquivo = criar_nome_arquivo(i, legenda['texto'])
        caminho_saida = Path(pasta_saida) / nome_arquivo
        
        # Salva o trecho
        trecho.export(caminho_saida, format='mp3')
        
        print(f"[{i}/{len(legendas)}] Salvo: {nome_arquivo}")
    
    print("Concluído!")

if __name__ == '__main__':
    # ============================================
    # CONFIGURE AQUI OS CAMINHOS
    # ============================================
    
    # Caminho do arquivo de áudio (MP3, WAV, etc.)
    # Exemplo: r'C:\MeusProjetos\Audio\episodio_original.mp3'
    AUDIO_PATH = r''
    
    # Caminho do arquivo SRT de legendas
    # Exemplo: r'C:\MeusProjetos\Legendas\episodio.srt'
    SRT_PATH = r''
    
    # Pasta onde os áudios fatiados serão salvos
    # Exemplo: r'C:\MeusProjetos\AudiosFatiados'
    OUTPUT_PATH = r''
    
    # ============================================
    
    # Executa o script
    slice_audio(AUDIO_PATH, SRT_PATH, OUTPUT_PATH)
