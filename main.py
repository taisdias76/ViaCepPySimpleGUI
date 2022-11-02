from PySimpleGUI import PySimpleGUI as sg

import consultaAPI

result = ''
sg.theme('LightGreen2')
layout = [
    [sg.Text('CEP'), sg.Input(key='cep', size=(25, 1))],
    [sg.Button('Pesquisar')]
]

janela = sg.Window('Consulta CEP', layout, element_justification='c')

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Pesquisar':
        if len(valores['cep']) != 8:
            sg.popup('Resultado', 'CEP inválido. Informe um CEP de 8 dígitos.')
        else:
            result = consultaAPI.main(valores['cep'])
            if result is None:
                sg.popup('CEP inválido.')
            else:
                sg.popup('Resultado', 'CEP: ' + result['cep'], 'Logragouro: ' + result['logradouro'],
                         'Localidade: ' + result['localidade'])
