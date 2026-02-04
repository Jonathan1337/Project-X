"""
Audio Split - Extrator de Áudio de Vídeo

Extrai a faixa de áudio de um arquivo de vídeo e salva como MP3.
Útil para extrair o áudio de episódios antes do fatiamento com audio_slicer.py.

Uso:
    1. Configure INPUT_PATH com o caminho do vídeo
    2. Execute: python audio_split.py
    3. O arquivo MP3 será salvo no mesmo diretório do script

Dependências:
    - moviepy (pip install moviepy)
    - ffmpeg instalado no sistema
"""

from moviepy import VideoFileClip
from pathlib import Path


# ============== CONFIGURAÇÃO ==============
# Caminho do arquivo de vídeo (MP4, MKV, AVI, etc.)
INPUT_PATH = r''
# ==========================================


if __name__ == '__main__':
    if not INPUT_PATH:
        print("ERRO: Configure INPUT_PATH com o caminho do vídeo!")
        print("Exemplo: INPUT_PATH = r'C:\\Videos\\episodio.mp4'")
    else:
        input_filename = Path(INPUT_PATH).stem
        output_path = f"{input_filename}.mp3"
        
        print(f"Extraindo áudio de: {INPUT_PATH}")
        print(f"Salvando como: {output_path}")
        
        video = VideoFileClip(INPUT_PATH)
        video.audio.write_audiofile(output_path)
        
        print("Concluído!")