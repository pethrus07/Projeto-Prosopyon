import FreeSimpleGUI as sg
import cv2

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Contato')],
    [sg.Input(key='Contato')],
    [sg.Button('Mapeamento Facial', key='mapeamento')],
    [sg.Button('Cadastro')],
    [sg.Text('',key='mensagem')],
]



window= sg.Window('Prosopyon', layout=layout)

while True:
    event, values=window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'mapeamento':
        cap=cv2.VideoCapture(0)
    
        while True:
            ret, frame = cap.read()

            if ret == False:
                continue

            cv2.imshow('video frame', frame)

            key_pressed = cv2.waitKey(1) & 0xFF

            if key_pressed == ord('q'):
             break


cap.release()
cv2.destroyAllWindows()
