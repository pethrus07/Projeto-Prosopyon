"""Prosopyon: cadastro e login por reconhecimento facial, no terminal.

Fluxo: cadastra o rosto pela webcam, depois pede o nome e captura de novo
para conferir se o rosto bate com o cadastrado. As fotos ficam em PNG na
pasta `PASTA_IMAGENS`.

OpenCV e face_recognition sao importados dentro das funcoes que usam a
camera e o modelo. Assim o modulo pode ser importado (e testado) sem webcam
e sem compilar o dlib.
"""
import os

from rich.console import Console

console = Console()

# Uma pasta so para gravar e para ler. Antes o cadastro gravava em `imagens/`
# e o login lia de `images/`, entao o rosto cadastrado nunca era encontrado.
PASTA_IMAGENS = "imagens"

ENTER = 13
ESC = 27


def caminho_cadastro(nome):
    return os.path.join(PASTA_IMAGENS, f"{nome}.png")


def caminho_login(nome):
    return os.path.join(PASTA_IMAGENS, f"{nome}_desconhecido.png")


def capturar_rosto(destino, titulo, instrucao, pos_instrucao=(150, 20), escala=0.6):
    """Abre a webcam, marca os rostos e grava o quadro em `destino` no Enter.

    ESC fecha a janela. Devolve True se pelo menos uma foto foi gravada.
    """
    import cv2

    os.makedirs(os.path.dirname(destino) or ".", exist_ok=True)
    video_capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gravou = False
    font = cv2.FONT_HERSHEY_SIMPLEX

    while True:
        ret, frame = video_capture.read()
        if not ret:
            console.print("Nao foi possivel ler a camera.", style="bold red")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(frame, instrucao, pos_instrucao, font, escala, (0, 0, 0), 2, cv2.LINE_4)
        cv2.putText(frame, "- ESC para sair -", (250, 450), font, 0.6, (0, 0, 0), 2, cv2.LINE_4)
        cv2.imshow(titulo, frame)

        key = cv2.waitKey(1)
        if key == ESC:
            break
        elif key == ENTER:
            cv2.imwrite(destino, frame)
            gravou = True

    video_capture.release()
    cv2.destroyAllWindows()
    return gravou


def reconhece_face(caminho_foto):
    """Devolve (True, encodings) se achou rosto na foto, senao (False, [])."""
    import face_recognition as fr

    if not os.path.exists(caminho_foto):
        return False, []
    foto = fr.load_image_file(caminho_foto)
    rostos = fr.face_encodings(foto)
    if len(rostos) > 0:
        return True, rostos
    return False, []


def mensagem_resultado(resultados):
    """Traduz a saida de face_recognition.compare_faces numa mensagem."""
    if resultados == [True]:
        return "Usuario identificado!", "green bold"
    return "Usuario nao corresponde ao cadastrado!", "red bold"


def main():
    import face_recognition as fr

    # Cadastro
    console.print("Bem vindo ao ProsopyonCad", style="bold blue")
    nome_cad = input("Digite seu nome, por gentileza: ")
    console.print("Ok, agora abra o programa na barra de tarefas", style="bold red")
    capturar_rosto(caminho_cadastro(nome_cad), "Cadastro de Foto Base",
                   "Pressione Enter para capturar seu rosto")

    # Login
    print("\n" + "=" * 28)
    console.print("Seja bem vindo ao Prosopyon.login\n", style="bold green")
    nome_log = input("Digite seu nome cadastrado: ")
    console.print("Ok, agora abra o programa na barra de tarefas", style="bold red")
    capturar_rosto(caminho_login(nome_log), "video",
                   "Reconhecimento Facial, pressione Enter para capturar seu rosto.",
                   pos_instrucao=(10, 20), escala=0.5)

    # Comparacao
    desconhecido = reconhece_face(caminho_login(nome_log))
    if not desconhecido[0]:
        print("Nao foi encontrado nenhum rosto")
        return

    cadastrado = reconhece_face(caminho_cadastro(nome_cad))
    if not cadastrado[0]:
        print("Nao foi encontrado rosto na foto de cadastro")
        return

    resultados = fr.compare_faces([cadastrado[1][0]], desconhecido[1][0])
    texto, estilo = mensagem_resultado(resultados)
    console.print(f"{os.linesep}-> {texto}", style=estilo)
    if resultados == [True]:
        print("O rosto de", nome_cad, "foi reconhecido.")


if __name__ == "__main__":
    main()
