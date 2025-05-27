import FreeSimpleGUI as sg

layout = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Cargo')],
    [sg.Input(key='cargo')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Reconhecimento facial')],
    [sg.Button('Login')],
]

window= sg.Window('Prosopyon', layout=layout)

while True:
    event, values=window.read()
    if event == sg.WIN_CLOSED:
        break

if evento == 'Salvar':
        nome = valores['NOME']
        idade = valores['IDADE']

 with open('dados.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Nome: {nome}, Idade: {idade}\n')

        sg.popup('Dados salvos com sucesso!')
