# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.2.2] - 2026-02-10

### Corrigido
- **i18n:** Escape de `%` nas strings em pt-BR (`10%` → `10%%`) para evitar `ValueError: incomplete format`
- **UI:** Correção do slideshow no main menu

### Modificado
- **Characters:** Melhora na legibilidade e remoção de code smells em `characters.rpy`
- **Docs:** Correção do README (estrutura de projeto, arquitetura modular, arquivos faltantes)

---

## [1.2.1] - 2026-02-04

### Adicionado
- **Slideshow no Main Menu:** Implementação de slideshow dinâmico na tela principal
- **Seletor de Idiomas:** Tela de seleção de idioma (EN/PT-BR) via `language_select.rpy`
- **Localização pt-BR:** Tradução completa do jogo para Português Brasileiro

### Modificado
- README atualizado para versão 1.2.1

### Removido
- Scripts desnecessários removidos do repositório

---

## [1.2.0] - 2026-02-04

### Adicionado
- **Sistema Auto Voice**: Implementação de sistema dinâmico de mapeamento de voz que carrega arquivos de áudio automaticamente baseado nos IDs únicos de diálogo, eliminando a necessidade de tags `voice` manuais
- **Auto Translator** (`tools/auto_translator/`): Ferramenta de tradução automatizada utilizando Ollama (IA local) para traduzir arquivos de localização do Ren'Py
  - Suporte a três formatos: old/new, diálogos com personagem e narrações
  - Modo dry-run para simulação de traduções
  - Documentação completa em `auto_translator.md`
- **Suporte a Português (pt-BR)**: Estrutura de tradução completa em `game/tl/portuguese/`
- **Novas ferramentas de processamento de áudio**:
  - `audio_split.py`: Extração de faixas de áudio de arquivos de vídeo (MoviePy)
  - `audio_slicer.py`: Fatiamento automático de áudio baseado em timestamps de legendas .SRT (pydub)
  - `voice_renamer.py`: Associação automática de áudios a IDs do Ren'Py via Fuzzy Matching
  - `audio_converter.py`: Conversão em massa de MP3 para OGG Vorbis
- **Documentação Auto Voice**: Guia completo em `tools/AUTO_VOICE_GUIDE.md` descrevendo o workflow de implementação

### Modificado
- Reorganização da estrutura de pastas de áudio para `game/audio/voice/{scene_name}/`
- Atualização do `options.rpy` com função de mapeamento dinâmico de vozes
- README.md atualizado com documentação das novas ferramentas e competências técnicas

### Técnico
- Integração com Ollama para tradução offline via modelo `gemma3:4b`
- Sistema de cache de arquivos de voz para performance otimizada
- Expressões regulares avançadas para parsing de arquivos de tradução do Ren'Py

---

## [1.0.2] - 2026-01-26

### Adicionado
- Paleta de cores temática Dunder Mifflin (Azul Royal, Grafite, Bege)
- Fonte American Typewriter para elementos de interface
- Sombreado sutil nos botões de navegação

### Modificado
- Reduzido tamanho do título do menu principal (75→55)
- Ajustado dimensionamento dos choice buttons para melhor proporção na tela
- Removido overlay transparente do menu principal para melhor legibilidade
- Corrigida cor dos botões Yes/No na tela de confirmação

## [1.0.1] - 2026-01-24

### Adicionado
- Arquivo dedicado para definições de personagens (`characters.rpy`)
- Splashscreen customizada em arquivo separado (`splashscreen.rpy`)

### Modificado
- Melhorado design visual das dialogue boxes (cores, bordas e transparência)
- Modularização da codebase: separação de responsabilidades entre arquivos
- Correção de link quebrado no README

### Corrigido
- Ajuste na lógica condicional do final (good/bad ending)
- Correção de erros de digitação no `script.rpy` e frames incorretos

## [1.0.0] - 2026-01-21

### Adicionado
- Release inicial do projeto "Get Your Raise"
- Sistema de afinidade e escolhas ramificadas
- Scripts de automação Python para pipeline de assets:
  - `script_normalizer.py`: Extração e limpeza de legendas (.srt)
  - `printscreemer.py`: Extração automatizada de frames de vídeo usando OpenCV

---

[1.2.2]: https://github.com/Jonathan1337/Project-X/compare/v1.2.1...v1.2.2
[1.2.1]: https://github.com/Jonathan1337/Project-X/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/Jonathan1337/Project-X/compare/v1.0.2...v1.2.0
[1.0.2]: https://github.com/Jonathan1337/Project-X/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/Jonathan1337/Project-X/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/Jonathan1337/Project-X/releases/tag/v1.0.0
