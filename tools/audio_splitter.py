"""
Audio Splitter Tool
-------------------
Divide arquivos de áudio em múltiplas partes baseado em pontos de corte.
Útil quando um único áudio contém múltiplas falas de personagens.

Uso:
    python audio_splitter.py <arquivo_audio> <ponto_corte_ms> <nome1> <nome2>
    
Exemplo:
    python audio_splitter.py "audio.ogg" 1500 "jan_michael.ogg" "michael_no.ogg"
"""

from pydub import AudioSegment
import os
import sys


def get_audio_info(input_file):
    """Mostra informações do áudio para ajudar a encontrar o ponto de corte."""
    audio = AudioSegment.from_file(input_file)
    print(f"Arquivo: {input_file}")
    print(f"Duração: {len(audio)}ms ({len(audio)/1000:.2f}s)")
    print(f"Canais: {audio.channels}")
    print(f"Sample Rate: {audio.frame_rate}Hz")
    return audio


def split_audio(input_file, split_points_ms, output_names, output_dir=None):
    """
    Divide um arquivo de áudio em múltiplas partes.
    
    Args:
        input_file: Caminho do arquivo de áudio original
        split_points_ms: Lista de pontos de corte em milissegundos
                        Ex: [1500] divide em 0-1500ms e 1500-fim
        output_names: Lista de nomes para os arquivos de saída
        output_dir: Diretório de saída (opcional, usa o mesmo do input)
    """
    audio = AudioSegment.from_file(input_file)
    
    # Valida número de outputs
    expected_outputs = len(split_points_ms) + 1
    if len(output_names) != expected_outputs:
        raise ValueError(
            f"Número de nomes de saída ({len(output_names)}) deve ser "
            f"igual ao número de segmentos ({expected_outputs})"
        )
    
    # Define diretório de saída
    if output_dir is None:
        output_dir = os.path.dirname(input_file) or "."
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Adiciona início e fim aos pontos de corte
    points = [0] + sorted(split_points_ms) + [len(audio)]
    
    created_files = []
    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]
        segment = audio[start:end]
        
        output_path = os.path.join(output_dir, output_names[i])
        
        # Detecta formato pelo nome do arquivo
        ext = os.path.splitext(output_names[i])[1].lower().lstrip('.')
        if ext == 'ogg':
            segment.export(output_path, format="ogg", codec="libvorbis")
        else:
            segment.export(output_path, format=ext)
        
        duration_ms = end - start
        print(f"✓ Criado: {output_path} ({duration_ms}ms)")
        created_files.append(output_path)
    
    return created_files


def interactive_mode():
    """Modo interativo para dividir áudios."""
    print("=" * 50)
    print("  Audio Splitter - Modo Interativo")
    print("=" * 50)
    
    input_file = input("\nCaminho do arquivo de áudio: ").strip().strip('"')
    
    if not os.path.exists(input_file):
        print(f"Erro: Arquivo não encontrado: {input_file}")
        return
    
    audio = get_audio_info(input_file)
    
    print("\n" + "-" * 50)
    print("Digite os pontos de corte em milissegundos (separados por vírgula)")
    print("Exemplo: 1500 (para dividir em 2 partes)")
    print("Exemplo: 1500, 3000 (para dividir em 3 partes)")
    
    points_input = input("\nPontos de corte (ms): ").strip()
    split_points = [int(p.strip()) for p in points_input.split(",")]
    
    num_segments = len(split_points) + 1
    print(f"\nO áudio será dividido em {num_segments} partes.")
    print("Digite os nomes dos arquivos de saída:")
    
    output_names = []
    for i in range(num_segments):
        name = input(f"  Segmento {i+1}: ").strip()
        if not name.endswith(('.ogg', '.mp3', '.wav')):
            name += '.ogg'
        output_names.append(name)
    
    output_dir = input("\nDiretório de saída (Enter para mesmo local): ").strip().strip('"')
    if not output_dir:
        output_dir = None
    
    print("\n" + "-" * 50)
    print("Dividindo áudio...")
    split_audio(input_file, split_points, output_names, output_dir)
    print("\nConcluído!")


def main():
    if len(sys.argv) < 2:
        interactive_mode()
        return
    
    if sys.argv[1] in ['-h', '--help']:
        print(__doc__)
        return
    
    if sys.argv[1] == '--info':
        if len(sys.argv) < 3:
            print("Uso: python audio_splitter.py --info <arquivo>")
            return
        get_audio_info(sys.argv[2])
        return
    
    # Modo linha de comando
    if len(sys.argv) < 5:
        print("Uso: python audio_splitter.py <arquivo> <ponto_ms> <saida1> <saida2> [...]")
        print("     python audio_splitter.py --info <arquivo>")
        print("     python audio_splitter.py  (modo interativo)")
        return
    
    input_file = sys.argv[1]
    split_point = int(sys.argv[2])
    output_names = sys.argv[3:]
    
    split_audio(input_file, [split_point], output_names)


if __name__ == "__main__":
    main()
