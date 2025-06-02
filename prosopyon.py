import FreeSimpleGUI as sg
import cv2
import face_recognition as fr
import os
from rich import print
from rich.console import Console

console = Console()

##Cadastro

console.print('Bem vindo ao ProsopyonCad', style='bold blue')
name_cad = input('Digite seu nome, por gentileza: ')
console.print('Ok, Agora abra o programa na barra de tarefas', style="bold red")

video_capture = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#no tocante a rostos

    faces = faceCascade.detectMultiScale(
        gray, 
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(
        frame, 
        'Pressione Enter para capturar seu rosto',
        (150,20),
        font, 0.6,
        (0,0,0),
        2,
        cv2.LINE_4
    )

    cv2.putText(
        frame, 
        '- ESC para sair-',
        (250, 450),
        font, 0.6,
        (0,0,0),
        2,
        cv2.LINE_4
    )

    cv2.imshow('Cadastro de Foto Base', frame)

    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == 13:
        cv2.imwrite(f'imagens/{name_cad}.png', frame)

video_capture.release()
cv2.destroyAllWindows()
