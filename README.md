# Get Your Raise 1.0.1 - The Office Visual Novel Tribute

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

### 🛠️ Automação & Tooling (Python Scripts)
Para otimizar o fluxo de desenvolvimento e eliminar tarefas manuais, desenvolvi uma suíte de scripts em Python localizada na pasta `/tools`, simulando uma pipeline de produção real:

*   **`script_normalizer.py` (Subtitle ETL Pipeline):** Um script de automação que realiza o parsing de arquivos de legenda (`.srt`). Ele extrai blocos de diálogo específicos usando lógica condicional, sanitiza o texto removendo tags HTML via Regex e exporta as falas limpas, acelerando a migração de diálogos originais da série para o roteiro do jogo.
*   **`printscreemer.py` (Video Frame Extraction):** Uma automação utilizando **OpenCV (cv2)** para processamento de vídeo. O script varre arquivos de episódios brutos e extrai frames automaticamente em intervalos regulares (amostragem de 1 frame/segundo), criando rapidamente um banco de imagens massivo para ser utilizado como assets de cenários e personagens na Visual Novel.

---

### [English] 🇺🇸

**Get Your Raise** is a Visual Novel inspired by *The Office*, developed as a technical case study. The main goal of this project is to showcase skills in **Software Engineering**, **Game Logic**, and **Python Automation**.

The player takes on the role of an employee trying to negotiate a raise, where every choice alters the internal game state and the narrative outcome through affinity systems.

### 🧩 Technical Competencies (Game Dev)
*   **Complex State Management:** Implementation of tracking variables (`jan_affinity`, `darryl_respect`) that control narrative branching in real-time.
*   **Python/Ren'Py Integration:** Utilization of native `python:` blocks within the engine for advanced conditional logic and persistent data manipulation.
*   **Modular Architecture:** Separation of concerns with dedicated scripts for definitions, screens (`screens.rpy`), and narrative flow (`script.rpy`), ensuring maintainability.
*   **Custom UI/UX:** Full customization of the Graphical User Interface (GUI) for thematic immersion.

### 🛠️ Automation & Tooling (Python Scripts)
To optimize the development workflow and eliminate manual tasks, I engineered a suite of Python scripts located in the `/tools` directory, acting as a production asset pipeline:

*   **`script_normalizer.py` (Subtitle ETL Pipeline):** An automation script that performs parsing of subtitle files (`.srt`). It extracts specific dialogue blocks using conditional logic, sanitizes text by removing HTML tags via Regex, and exports clean lines, accelerating the migration of original show dialogue into the game script.
*   **`printscreemer.py` (Video Frame Extraction):** An automation script leveraging **OpenCV (cv2)** for video processing. It parses raw video episodes and automatically extracts frames at regular intervals (1 frame/second sampling rate), rapidly generating a massive dataset of images to be used as background and character assets for the Visual Novel.

---

## 📂 Estrutura do Projeto / Project Structure

```text
/
├── game/                   # Core game files (Ren'Py assets & scripts)
│   ├── images/
│   ├── audio/
│   ├── script.rpy          # Main narrative flow
│   └── screens.rpy         # UI Layout definitions
│
├── tools/                  # Python Automation Suite ⚙️
│   ├── printscreemer.py    # Image processing automation
│   └── script_normalizer.py # Text parsing & normalization
│
└── README.md
🚀 Como Rodar / How to Run
Clone o repositório / Clone the repository:

bash
git clone https://github.com/seu-usuario/get-your-raise.git
Baixe o Ren'Py SDK.

Aponte o diretório do projeto no launcher do Ren'Py e clique em "Launch Project".

⚖️ Disclaimer / Aviso Legal
Non-profit fan project for educational and portfolio purposes only.
The Office and all related characters, names, and indicia are property of NBCUniversal. This software is not affiliated with, endorsed by, or connected to the original creators.

Este é um projeto de fã, sem fins lucrativos, criado estritamente para fins de portfólio e estudo.
