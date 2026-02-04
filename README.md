# Get Your Raise 1.2.0 - The Office Visual Novel Tribute

> *"I’m not superstitious, but I am a little stitious." — Michael Scott*

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg) ![Ren'Py](https://img.shields.io/badge/Engine-Ren%27Py-pink.svg) ![Status](https://img.shields.io/badge/Status-Completed-success.svg)

---

### [Português] 🇧🇷

**Get Your Raise** é uma Visual Novel inspirada na série *The Office*, desenvolvida como um estudo de caso técnico. O objetivo principal deste projeto é demonstrar competências em **Engenharia de Software**, **Lógica de Jogos** e **Automação com Python**.

O jogador assume o papel de um funcionário tentando conseguir um aumento, onde cada escolha altera o estado interno do jogo e o desfecho da narrativa através de sistemas de afinidade.

### 🧩 Competências Técnicas (Game Dev)
*   **Gestão de Estado Complexa:** Implementação de variáveis de rastreamento (`jan_affinity`, `darryl_respect`) que controlam a ramificação da história (branching narrative) em tempo real.
*   **Integração Python/Ren'Py:** Uso de blocos `python:` nativos para lógica condicional avançada e manipulação de dados persistentes.
*   **Arquitetura Modular:** Separação de responsabilidades com scripts dedicados para definições, telas (`screens.rpy`) e fluxo narrativo (`script.rpy`), facilitando a manutenção.
*   **UI/UX Personalizada:** Customização completa da interface gráfica (GUI) para imersão temática.
*   **Sistema de Auto Voice:** Implementação de um sistema dinâmico de mapeamento de voz (`options.rpy`) que carrega automaticamente arquivos de áudio baseados nos IDs únicos de diálogo, eliminando a necessidade de tags manuais `voice` em cada linha.

### 🛠️ Automação & Tooling (Python Scripts)
Para otimizar o fluxo de desenvolvimento e eliminar tarefas manuais, desenvolvi uma suíte de scripts em Python localizada na pasta `/tools`, simulando uma pipeline de produção real:

*   **`printscreemer.py` (Video Frame Extraction):** Uma automação utilizando **OpenCV (cv2)** para processamento de vídeo. O script varre arquivos de episódios brutos e extrai frames automaticamente em intervalos regulares (amostragem de 1 frame/segundo), criando rapidamente um banco de imagens massivo para ser utilizado como assets de cenários e personagens na Visual Novel.
*   **`audio_split.py` (Video Audio Extraction):** Automação simples utilizando **MoviePy** para extrair a faixa de áudio de arquivos de vídeo (MP4) e convertê-la para MP3, facilitando a obtenção do áudio bruto dos episódios para posterior processamento.
*   **`audio_slicer.py` (Audio Slicing Automation):** Script que utiliza timestamps de arquivos `.srt` para recortar automaticamente faixas de áudio longas em clipes individuais de fala, sincronizados com o diálogo.
*   **`voice_renamer.py` (Voice Asset Management):** Ferramenta de organização que utiliza *Fuzzy Matching* para associar arquivos de áudio recortados às linhas de diálogo do script Ren'Py, renomeando-os automaticamente com o ID único da cena (ex: `scene_1_2d85d9a7.ogg`) e movendo-os para a estrutura de pastas correta.
*   **`audio_converter.py` (Asset Optimization):** Utilitário de conversão em massa (Batch Processing) que transcodifica arquivos MP3 para OGG Vorbis, otimizando o tamanho dos assets de áudio sem perda perceptível de qualidade.
*   **`auto_translator/` (Automated Translation):** Sistema de tradução automatizada que utiliza **Ollama** (IA local) para traduzir arquivos de localização do Ren'Py. O script identifica padrões de tradução vazios via *Regex* e preenche automaticamente com traduções geradas pelo modelo de linguagem, acelerando o processo de localização (i18n).

---

### [English] 🇺🇸

**Get Your Raise** is a Visual Novel inspired by *The Office*, developed as a technical case study. The main goal of this project is to showcase skills in **Software Engineering**, **Game Logic**, and **Python Automation**.

The player takes on the role of an employee trying to negotiate a raise, where every choice alters the internal game state and the narrative outcome through affinity systems.

### 🧩 Technical Competencies (Game Dev)
*   **Complex State Management:** Implementation of tracking variables (`jan_affinity`, `darryl_respect`) that control narrative branching in real-time.
*   **Python/Ren'Py Integration:** Utilization of native `python:` blocks within the engine for advanced conditional logic and persistent data manipulation.
*   **Modular Architecture:** Separation of concerns with dedicated scripts for definitions, screens (`screens.rpy`), and narrative flow (`script.rpy`), ensuring maintainability.
*   **Custom UI/UX:** Full customization of the Graphical User Interface (GUI) for thematic immersion.
*   **Auto Voice System:** Implementation of a dynamic voice mapping system (`options.rpy`) that automatically loads audio files based on unique dialogue IDs, eliminating the need for manual `voice` tags on every line.

### 🛠️ Automation & Tooling (Python Scripts)
To optimize the development workflow and eliminate manual tasks, I engineered a suite of Python scripts located in the `/tools` directory, acting as a production asset pipeline:

*   **`printscreemer.py` (Video Frame Extraction):** An automation script leveraging **OpenCV (cv2)** for video processing. It parses raw video episodes and automatically extracts frames at regular intervals (1 frame/second sampling rate), rapidly generating a massive dataset of images to be used as background and character assets for the Visual Novel.
*   **`audio_split.py` (Video Audio Extraction):** A simple automation utilizing **MoviePy** to extract audio tracks from video files (MP4) and convert them to MP3, streamlining the acquisition of raw episode audio for further processing.
*   **`audio_slicer.py` (Audio Slicing Automation):** A script utilizing `.srt` file timestamps to automatically slice long audio tracks into individual speech clips, perfectly synchronized with expected dialogue.
*   **`voice_renamer.py` (Voice Asset Management):** A management tool that uses *Fuzzy Matching* to query sliced audio files against Ren'Py script dialogue lines, automatically renaming them with unique scene IDs (e.g., `scene_1_2d85d9a7.ogg`) and sorting them into the correct directory structure.
*   **`audio_converter.py` (Asset Optimization):** A batch processing utility that transcoding MP3 files to OGG Vorbis, optimizing audio asset size without noticeable quality loss.
*   **`auto_translator/` (Automated Translation):** An automated translation system leveraging **Ollama** (local AI) to translate Ren'Py localization files. The script identifies empty translation patterns via *Regex* and automatically fills them with AI-generated translations, accelerating the localization (i18n) process.

---

## 📂 Estrutura do Projeto / Project Structure

```text
/
├── dialogue.tab                         # Dialogue ID mapping file
├── game/                                # Core game files (Ren'Py assets & scripts)
│   ├── images/                          # Game images and backgrounds
│   ├── audio/                           # Music and sound effects
│   │   └── voice/                       # Auto Voice audio files (OGG)
│   ├── fonts/                           # Custom fonts
│   ├── gui/                             # GUI assets
│   ├── scenes/                          # Narrative scenes scripts
│   │   ├── scene_1_michael_office.rpy
│   │   ├── scene_2_meeting_room.rpy
│   │   ├── scene_3_general_office.rpy
│   │   ├── scene_4_michael_office.rpy
│   │   ├── scene_5_phone_call.rpy
│   │   ├── scene_6_corporate_lobby.rpy
│   │   ├── scene_7_jan_negotiation.rpy
│   │   ├── scene_8_good_ending.rpy
│   │   └── scene_9_bad_ending.rpy
│   │
│   ├── script.rpy                       # Main entry point (label start)
│   ├── characters.rpy                   # Character definitions
│   ├── screens.rpy                      # UI Layout definitions
│   ├── gui.rpy                          # GUI configuration
│   ├── options.rpy                      # Game options and config
│   └── splashscreen.rpy                 # Initial warning screen
│
├── tools/                               # Python Automation Suite ⚙️
│   ├── printscreemer.py                 # Video frame extraction
│   ├── audio_split.py                   # Video audio extraction
│   ├── audio_slicer.py                  # Audio slicing utility
│   ├── voice_renamer.py                 # Voice asset management
│   ├── audio_converter.py               # Audio format converter
│   ├── AUTO_VOICE_GUIDE.md              # Auto Voice documentation
│   └── auto_translator/                 # Automated Translation Tool 🌐
│       ├── auto_translator.py           # Main translation script
│       └── auto_translator.md           # Tool documentation
│
└── README.md

```

---

## 📐 Convenções de Código / Code Conventions

### Nomenclatura / Naming Conventions
Este projeto segue o padrão **snake_case** para garantir consistência e legibilidade:

| Elemento | Convenção | Exemplo |
|----------|-----------|---------|
| Arquivos de cena | `scene_N_description.rpy` | `scene_1_michael_office.rpy` |
| Labels | `snake_case` | `label scene_1:`, `label good_ending:` |
| Variáveis | `snake_case` | `jan_affinity`, `darryl_respect` |
| Jumps/Calls | `snake_case` | `jump scene_2`, `call good_ending` |

### Estrutura de Cenas / Scene Structure
Cada arquivo de cena segue o padrão:
```renpy
#CENA N: DESCRIÇÃO DA CENA

label scene_N:
    # Conteúdo da cena
    jump scene_N+1
```

---

## 🚀 Como Rodar / How to Run

1. Clone o repositório / Clone the repository:
```bash
git clone https://github.com/Jonathan1337/Project-X.git
```

2. Baixe o [Ren'Py SDK](https://www.renpy.org/latest.html).

3. Aponte o diretório do projeto no launcher do Ren'Py e clique em "Launch Project".

---

## ⚖️ Disclaimer / Aviso Legal

> **Non-profit fan project for educational and portfolio purposes only.**
> *The Office* and all related characters, names, and indicia are property of NBCUniversal. This software is not affiliated with, endorsed by, or connected to the original creators.

> **Este é um projeto de fã, sem fins lucrativos, criado estritamente para fins de portfólio e estudo.**
> *The Office* e todos os personagens, nomes e elementos relacionados são propriedade da NBCUniversal.
