import cv2
import os


video_name = r"video_input"
folder_out = "meus_prints"

def extrair_frames():
    if not os.path.exists(video_name):
        print(f"ERRO: Não encontrei o arquivo '{video_name}' nesta pasta.")
        print("Certifique-se de que o vídeo está na mesma pasta que este script.")
        return

    if not os.path.exists(folder_out):
        os.makedirs(folder_out)

    cap = cv2.VideoCapture(video_name)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    if fps == 0:
        print("Erro: Não foi possível ler o FPS do vídeo.")
        return

    print(f"Iniciando... FPS do vídeo: {fps}")
    
    frame_atual = 0
    salvos = 0

    while True:
        sucesso, frame = cap.read()
        if not sucesso: break

        if frame_atual % fps == 0:
            arquivo = f"{folder_out}/frame_{salvos}.jpg"
            cv2.imwrite(arquivo, frame)
            print(f"Capturado: {arquivo}")
            salvos += 1

        frame_atual += 1

    cap.release()
    print("Processo finalizado!")

if __name__ == "__main__":
    extrair_frames()