import FreeSimpleGUI as sg
import face_recognition as fr

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Cargo')],
    [[sg.Combo(['Operário', 'Supervisor', 'Gerente'], default_value='Operário', key='cargo')]],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Reconhecimento facial', key='reconhecimentofacial')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]

window= sg.Window('Prosopyon', layout=layout)

while True:
    event, values=window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        senha_correta = '123456'
        usuario_correto = 'Jeofton'
        cargo_correto = 'Gerente'
        usuario = values['usuario']
        senha = values['senha']   
        cargo = values['cargo']
        if senha == senha_correta and usuario == usuario_correto and cargo == cargo_correto:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('senha ou usuario incorreto')
