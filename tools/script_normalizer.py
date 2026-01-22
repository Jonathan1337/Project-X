import re

caminho_do_arquivo = r"input"

def extrair_legendas(arquivo_entrada, arquivo_saida, numero_inicial):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        blocos = conteudo.split('\n\n')

        with open(arquivo_saida, 'w', encoding='utf-8') as f_out:
            for bloco in blocos:
                linhas = bloco.strip().split('\n')
                
                if len(linhas) >= 3:
                    try:
                        primeira_linha = linhas[0].strip().replace('\ufeff', '') 
                        
                        if not primeira_linha.isdigit():
                            continue
                            
                        indice_atual = int(primeira_linha)

                        if indice_atual >= numero_inicial:
                            linhas_texto = linhas[2:]
                            
                            texto_limpo = " ".join(linhas_texto)
                            texto_limpo = re.sub(r'<.*?>', '', texto_limpo)

                            f_out.write(f"{texto_limpo}\n")
                            
                    except ValueError:
                        continue

        print(f"Extração concluída! Salvo em '{arquivo_saida}'.")
        
    except FileNotFoundError:
        print(f"ERRO: Não encontrei o arquivo em: {arquivo_entrada}")

arquivo_saida_txt = "frases_extraidas.txt"
extrair_legendas(caminho_do_arquivo, arquivo_saida_txt, 317)