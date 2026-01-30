# Implementação do Auto Voice - Project X

Este documento descreve como o sistema de **Auto Voice** foi implementado no projeto "Project X" (Get Your Raise) e como utilizá-lo para adicionar vozes aos personagens automaticamente.

## 1. O que é o Auto Voice?

O Auto Voice é um recurso do Ren'Py que toca arquivos de voz automaticamente quando uma linha de diálogo é exibida, sem a necessidade de adicionar comandos `voice "arquivo.mp3"` manualmente em cada linha do script.

No nosso projeto, configuramos o Auto Voice para buscar arquivos de áudio baseados no **ID da linha de diálogo**.

## 2. Como Funciona (Técnico)

### 2.1. Identificadores de Diálogo (Dialogue IDs)
Cada linha de diálogo no script Ren'Py possui um identificador único, gerado automaticamente ou manualmente. Exemplo dos nossos scripts:

```renpy
# game/scenes/scene_1_michael_office.rpy
scene_1_2d85d9a7 "Tactic number six."
```

Neste caso, o ID é **`scene_1_2d85d9a7`**.

### 2.2. O Mapeador de Vozes (`options.rpy`)
No arquivo `game/options.rpy`, implementamos um script Python personalizado que:

1.  **Inicialização**: Ao abrir o jogo, ele varre recursivamente a pasta `game/audio/voice/`.
2.  **Indexação**: Ele encontra todos os arquivos `.ogg` e cria um "mapa" (dicionário) onde a chave é o nome do arquivo (sem extensão) e o valor é o caminho completo.
    *   Exemplo: Arquivo `game/audio/voice/scene_1/scene_1_2d85d9a7.ogg`
    *   É mapeado para o ID `scene_1_2d85d9a7`.
3.  **Execução**: Quando o jogo exibe um texto com ID `scene_1_2d85d9a7`, o Ren'Py consulta nossa função `buscar_voz`, que retorna o arquivo de áudio correspondente instantaneamente.

## 3. Fluxo de Trabalho (Workflow)

Para este projeto, o processo de implementação das vozes seguiu estas etapas específicas:

### Passo 1: Extração dos Diálogos no Ren'Py
Utilizamos a ferramenta nativa do Ren'Py Launcher (**Generate Translations**) para gerar o arquivo `dialogue.tab` na raiz do projeto. Este arquivo contém a relação entre o texto apresentado e seu ID único.

### Passo 2: Extração do Áudio do Episódio
Obtivemos o episódio original e extraímos a faixa de áudio completa (geralmente usando ffmpeg ou software de edição) para um arquivo de alta qualidade (ex: `.mp3` ou `.wav`).

### Passo 3: Fatiamento do Áudio (Slicing)
Ferramenta utilizada: **`tools/audio_slicer.py`**

Este script Python processa o áudio bruto usando o arquivo de legendas (`.srt`) original:
1.  Lê os *timestamps* (início e fim) de cada linha no SRT.
2.  Recorta o áudio original nestes intervalos exatos.
3.  Salva os trechos individualmente na pasta de saída.

> **Requisito:** O script utiliza a biblioteca `pydub`, que requer o **FFmpeg** instalado no sistema.

### Passo 4: Match e Organização
Ferramenta utilizada: **`tools/voice_renamer.py`**

Este script automatiza o processo de associação e organização:
1.  Lê o texto de cada áudio fatiado e compara com as linhas do `dialogue.tab`.
2.  Usa algoritmos de *Fuzzy Matching* (similaridade de texto) para encontrar o ID correto do Ren'Py para cada arquivo de áudio.
3.  **Renomeia** o arquivo para o formato `{ID}.mp3` (ex: `scene_1_2d85d9a7.mp3`).
4.  **Move** o arquivo para a estrutura de pastas correta: `game/audio/voice/scene_X/`.

### Passo 5: Ativação do Auto Voice
Arquivo modificado: **`game/options.rpy`**

Implementamos uma função Python em `init python` que:
1.  Escaneia a pasta `game/audio/voice/` ao iniciar o jogo.
2.  Cria um mapa virtual associando cada **ID** ao caminho do arquivo de áudio encontrado.
3.  Define `config.auto_voice` para usar essa função de busca, garantindo que o áudio correto toque sempre que a linha de diálogo correspondente aparecer na tela.

## 4. Referência das Ferramentas

| Ferramenta | Descrição | Dependências |
| :--- | :--- | :--- |
| `tools/audio_slicer.py` | Corta áudios longos baseado em legendas .SRT | Python, pydub, FFmpeg |
| `tools/voice_renamer.py` | Associa áudios a IDs do Ren'Py e organiza pastas | Python standard lib |
| `game/options.rpy` | Configuração do jogo que carrega as vozes dinamicamente | Ren'Py Engine |

## 4. Estrutura de Pastas de Áudio

Recomendamos manter os arquivos organizados por cena para facilitar a gestão, embora o script de mapeamento encontre arquivos em qualquer subpasta dentro de `voice/`.

```
game/
  audio/
    voice/
      scene_1/
        scene_1_2d85d9a7.mp3
        scene_1_45c91ad8.mp3
      scene_2/
        scene_2_30a65ae9.mp3
        ...
```

## 5. Solução de Problemas

*   **Voz não toca**:
    *   Verifique se o arquivo existe em `game/audio/voice`.
    *   Verifique se o nome do arquivo é **EXATAMENTE** igual ao ID da linha no script (sem a extensão).
    *   Verifique se o arquivo é `.mp3` (o script atual filtra apenas `.mp3`).
    *   Verifique o console (Shift+O) ou logs se houver erros de carregamento.

*   **Voz errada**:
    *   Provavelmente o ID foi alterado no script ou o arquivo foi nomeado incorretamente. Verifique o ID no script .rpy e compare com o nome do arquivo.
