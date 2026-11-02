[English](README.md) | Português

# Prosopyon

![status](https://img.shields.io/badge/status-arquivado%20(2026--11)-lightgrey)

Script de terminal para login por reconhecimento facial, em Python. Cadastra o rosto pela
webcam, depois pede o nome de novo, tira uma segunda foto e confere se o rosto bate com o
cadastrado.

## Status

**Arquivado (2026-11).** Trabalho em grupo da faculdade, de 2025 (três participantes,
visíveis no histórico de commits). Fica como registro e não recebe manutenção.

## Como funciona

1. Cadastro: a webcam abre, o Haar cascade do OpenCV marca o rosto, e o Enter grava o
   quadro em `imagens/<nome>.png`.
2. Login: a mesma captura grava `imagens/<nome>_desconhecido.png`.
3. Comparação: o `face_recognition` (dlib) codifica os dois rostos e compara.

Tudo roda numa execução só, sem banco. As fotos ficam no disco em PNG.

## Stack

Python, OpenCV (captura e detecção de rosto), face_recognition (codificação e comparação),
rich (saída no terminal).

## Como rodar

```bash
pip install -r requirements.txt   # o face_recognition compila o dlib: precisa de CMake e compilador C++
python prosopyon.py
```

Precisa de webcam.

## Testes

```bash
pip install pytest rich
pytest
```

Três testes cobrem o que não depende de câmera: os caminhos dos arquivos e a mensagem de
resultado. O CI (GitHub Actions) roda flake8 e pytest no Python 3.10 a 3.12, sem OpenCV e
sem dlib.

## O que ficou de aprendizado

- Em 2026-11 foi corrigido um bug real: o cadastro gravava em `imagens/` e o login lia de
  `images/`, então o rosto cadastrado nunca era encontrado. Agora os dois usam uma
  constante só.
- Código que roda no import não dá para testar. Levar o fluxo para funções, com os imports
  pesados dentro delas, deixou o módulo testável sem webcam.
- Comparar com uma foto cadastrada e a tolerância padrão é demonstração, não autenticação:
  não há prova de vida, e uma foto impressa passaria.

## Arquitetura

Casos de uso, processo e C4 em [docs/arquitetura/](docs/arquitetura/README.md).

## Licença

Todos os direitos reservados.
