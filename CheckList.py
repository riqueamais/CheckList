import PySimpleGUI as sg

#Criando o Layout
def criar_new_tarefa():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas', layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('CheckList',layout=layout, finalize = True)
#Criando a Janela
janela = criar_new_tarefa()
#Criando as regras dessa janela
while True:
    event,values = janela.read()
    if event == sg.WIN_CLOSED:
        break    
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'],[[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_new_tarefa()   