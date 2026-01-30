"""
Script de Conversão de Áudio MP3 para OGG (Vorbis)
Converte arquivos MP3 para OGG com qualidade configurável.
Requer ffmpeg instalado no sistema.
"""

import os
import subprocess
import shutil
from pathlib import Path


# ============== CONFIGURAÇÕES ==============
# Pasta com os arquivos MP3 a serem convertidos
INPUT_FOLDER = r"../game/audio/voice"

# Pasta para backup dos arquivos originais (será criada se não existir)
BACKUP_FOLDER = r"../game/audio/voice_backup_mp3"

# Qualidade do OGG Vorbis (0-10, onde 10 é a melhor qualidade)
# Baixa: 3-4 | Média: 5-6 | Alta: 7-8 | Máxima: 9-10
OGG_QUALITY = 5

# Deletar arquivos MP3 originais após conversão?
DELETE_ORIGINALS = True

# Processar subpastas recursivamente?
RECURSIVE = True

# ============================================


def check_ffmpeg():
    """Verifica se o ffmpeg está instalado."""
    try:
        result = subprocess.run(
            ['ffmpeg', '-version'],
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def get_file_size_mb(path):
    """Retorna o tamanho do arquivo em MB."""
    return os.path.getsize(path) / (1024 * 1024)


def convert_mp3_to_ogg(input_path, output_path, quality=6):
    """
    Converte um arquivo MP3 para OGG usando ffmpeg.
    Retorna True se sucesso, False se erro.
    """
    try:
        # Comando ffmpeg para converter MP3 para OGG Vorbis
        cmd = [
            'ffmpeg',
            '-i', str(input_path),
            '-c:a', 'libvorbis',
            '-q:a', str(quality),
            '-y',  # Sobrescrever se existir
            str(output_path)
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
        )
        
        if result.returncode == 0 and output_path.exists():
            return True
        else:
            print(f"  ERRO: {result.stderr[:200] if result.stderr else 'Erro desconhecido'}")
            return False
            
    except Exception as e:
        print(f"  ERRO ao converter {input_path}: {e}")
        return False


def main():
    # Verificar ffmpeg
    if not check_ffmpeg():
        print("=" * 60)
        print("ERRO: ffmpeg não encontrado!")
        print("=" * 60)
        print("\nPor favor, instale o ffmpeg:")
        print("  Windows: choco install ffmpeg")
        print("       ou: winget install ffmpeg")
        print("       ou: baixe de https://ffmpeg.org/download.html")
        print("\nCertifique-se de que o ffmpeg está no PATH do sistema.")
        return
    
    # Resolver caminhos relativos ao script
    script_dir = Path(__file__).parent
    input_folder = (script_dir / INPUT_FOLDER).resolve()
    backup_folder = (script_dir / BACKUP_FOLDER).resolve()
    
    print("=" * 60)
    print("     CONVERSOR DE ÁUDIO MP3 → OGG PARA VISUAL NOVEL")
    print("=" * 60)
    print(f"\nPasta de entrada:   {input_folder}")
    print(f"Pasta de backup:    {backup_folder}")
    print(f"Qualidade OGG:      {OGG_QUALITY}/10")
    print(f"Deletar originais:  {'Sim' if DELETE_ORIGINALS else 'Não'}")
    print(f"Modo recursivo:     {'Sim' if RECURSIVE else 'Não'}")
    print("-" * 60)
    
    # Verificar se a pasta de entrada existe
    if not input_folder.exists():
        print(f"\nERRO: Pasta de entrada não encontrada: {input_folder}")
        return
    
    # Listar todos os arquivos MP3
    if RECURSIVE:
        mp3_files = list(input_folder.rglob("*.mp3")) + list(input_folder.rglob("*.MP3"))
    else:
        mp3_files = list(input_folder.glob("*.mp3")) + list(input_folder.glob("*.MP3"))
    
    mp3_files = list(set(mp3_files))  # Remover duplicatas
    mp3_files.sort(key=lambda x: str(x))
    
    if not mp3_files:
        print("\nNenhum arquivo MP3 encontrado na pasta de entrada.")
        return
    
    print(f"\nEncontrados {len(mp3_files)} arquivos MP3 para converter.")
    
    # Calcular tamanho total original
    total_original = sum(get_file_size_mb(f) for f in mp3_files)
    print(f"Tamanho total original: {total_original:.2f} MB")
    
    # Confirmar com o usuário
    # response = input("\nDeseja continuar? (s/n): ").strip().lower()
    # if response != 's':
    #     print("Operação cancelada pelo usuário.")
    #     return
    
    # Criar pasta de backup
    backup_folder.mkdir(parents=True, exist_ok=True)
    print(f"\nCriando backup em: {backup_folder}")
    
    # Processar arquivos
    processed = 0
    errors = 0
    total_converted = 0.0
    
    for i, mp3_path in enumerate(mp3_files, 1):
        original_size = get_file_size_mb(mp3_path)
        
        # Calcular caminho relativo para manter estrutura de pastas no backup
        relative_path = mp3_path.relative_to(input_folder)
        
        # Backup do original
        backup_path = backup_folder / relative_path
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        if not backup_path.exists():
            shutil.copy2(mp3_path, backup_path)
        
        # Definir caminho de saída (trocar extensão para .ogg)
        ogg_path = mp3_path.with_suffix('.ogg')
        
        print(f"[{i}/{len(mp3_files)}] Convertendo: {relative_path}...", end=" ")
        
        # Converter
        if convert_mp3_to_ogg(mp3_path, ogg_path, OGG_QUALITY):
            converted_size = get_file_size_mb(ogg_path)
            total_converted += converted_size
            processed += 1
            
            size_diff = original_size - converted_size
            sign = "+" if size_diff < 0 else "-"
            
            print(f"OK ({original_size:.2f}MB → {converted_size:.2f}MB, {sign}{abs(size_diff):.2f}MB)")
            
            # Deletar original se configurado
            if DELETE_ORIGINALS:
                mp3_path.unlink()
        else:
            errors += 1
            print("FALHOU")
            if ogg_path.exists():
                ogg_path.unlink()
    
    # Relatório final
    print("\n" + "=" * 60)
    print("                    RELATÓRIO FINAL")
    print("=" * 60)
    print(f"Arquivos convertidos:  {processed}/{len(mp3_files)}")
    print(f"Erros:                 {errors}")
    print(f"Tamanho original MP3:  {total_original:.2f} MB")
    print(f"Tamanho OGG:           {total_converted:.2f} MB")
    
    diff = total_original - total_converted
    if total_original > 0:
        percent = (diff / total_original) * 100
        if diff > 0:
            print(f"Espaço economizado:    {diff:.2f} MB ({percent:.1f}%)")
        else:
            print(f"Aumento de tamanho:    {-diff:.2f} MB ({-percent:.1f}%)")
    
    print(f"\nBackup MP3 salvo em: {backup_folder}")
    if not DELETE_ORIGINALS:
        print("\nNota: Os arquivos MP3 originais foram mantidos.")
        print("      Configure DELETE_ORIGINALS = True para removê-los.")
    print("=" * 60)


if __name__ == "__main__":
    main()
