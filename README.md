English | [Português](README.pt-BR.md)

# Prosopyon

![status](https://img.shields.io/badge/status-archived%20(2026--11)-lightgrey)

A terminal script for face recognition login, in Python. It registers a face from the
webcam, then asks for the name again, takes a second photo and checks whether the face
matches the registered one.

## Status

**Archived (2026-11).** A university group project from 2025 (three contributors, visible
in the commit history). It is kept as a record and is not maintained.

## How it works

1. Registration: the webcam opens, OpenCV's Haar cascade draws a box around the face, and
   Enter saves the frame to `imagens/<name>.png`.
2. Login: the same capture saves `imagens/<name>_desconhecido.png`.
3. Comparison: `face_recognition` (dlib) encodes both faces and compares them.

Everything runs in one execution, with no database. Photos stay on disk as PNG.

## Stack

Python, OpenCV (capture and face detection), face_recognition (encoding and comparison),
rich (terminal output).

## Running

```bash
pip install -r requirements.txt   # face_recognition builds dlib: needs CMake and a C++ compiler
python prosopyon.py
```

Needs a webcam.

## Tests

```bash
pip install pytest rich
pytest
```

Three tests cover what does not need a camera: file paths and the result message. CI
(GitHub Actions) runs flake8 and pytest on Python 3.10 to 3.12 without OpenCV or dlib.

## What was learned

- In 2026-11 a real bug was fixed: registration saved to `imagens/` and login read from
  `images/`, so the registered face was never found. Now both use one constant.
- Code that runs at import time cannot be tested. Moving the flow into functions and the
  heavy imports inside them made the module testable without a webcam.
- A face match with one registered photo and default tolerance is a demo, not
  authentication: there is no liveness check, and a printed photo would pass.

## Architecture

Use cases, process and C4 in [docs/arquitetura/](docs/arquitetura/README.md) (Portuguese).

## License

All rights reserved.
