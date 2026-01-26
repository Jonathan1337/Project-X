# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

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

[1.0.2]: https://github.com/Jonathan1337/Project-X/compare/v1.0.1...v1.0.2
[1.0.1]: https://github.com/Jonathan1337/Project-X/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/Jonathan1337/Project-X/releases/tag/v1.0.0
