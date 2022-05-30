#from curses import window
from tkinter import CENTER
import PySimpleGUI as sg
#import controller as ctr

#UAL_COLOR
def ual_color():
    #50,116,159
    # #32749f
    return "#32749f"
# Main Window
def mainmenu():
    sg.theme('SystemDefault')
    menu_def=['&Espetáculos', ['&Novo', '&Consultar']],['&Reservas',['&Nova Reserva', '&Consultar']],['&Receita', ['&Diária', '&Mensal']],['&Programa', ['&Sair']]
    layout=[[sg.Menu(menu_def, font='Lucida', pad=(10,10))],
        #[sg.ButtonMenu('', [['nf', 'op','om','---','rf','cl'],['New File', 'Open','Open Module','---','Recent Files','Close']],image_filename ='icon_biggrin.gif',border_width=5),sg.ButtonMenu('', [['rm', 'rc','sm','ps'],['Run', 'Run Module','Shell','Python module']],image_filename ='icon_cry.gif',background_color='teal'),sg.ButtonMenu('Terminate', [['ex', 'cl','---','ab'],['Exit', 'Close','---','About us...']])],
        #[sg.Multiline(size=(80,10),tooltip='Write your Text here')],
        #[sg.Text('File Name'),sg.Input(),sg.OptionMenu(values=['.txt','.pdf','.gif', '.jpg','.mp4','.gif','.dat','.sql'],size=(4,8),default_value='.doc',key='ftype')],
        #[sg.Button('Nova', key='_new_', visible=True, font=('Lucida',20), button_color=('white', 'red'), size=(4, 1))],
        #[sg.Image(r'logo_ual.png')]
        ]
    window = sg.Window("AED - Arquitetura e Estrutura de Dados", layout, resizable=True, location=(0,0), size=(800,600), keep_on_top=True).finalize()
    window.Maximize()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=='_exit_':
            window.close()
        elif event == "_new_":
            apresentar_sala()
        elif event == "Novo":
            apresentar_sala()
        elif event == "Nova Reserva":
            apresentar_sala()
        elif event == "Sair":
            window.close()
            break

def segunda():
    layout=[[sg.Button('Sair', key='_exit_', visible=True, font=('Lucida',20), button_color=('white', ual_color()), size=(4, 1))]]
    window = sg.Window("Segunda", layout, modal=True, text_justification=CENTER, element_justification=CENTER, location=(0,0), size=(600,300), keep_on_top=True).finalize()
    window.BringToFront()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=='_exit_':
            window.close()
            break


def apresentar_sala():
    linha = 1
    for i in range(10):
        coluna = 'A'
        lugar = coluna + linha
        layout=[[sg.Button(lugar, key=lugar, visible=True, font=('Lucida',20), button_color=('white', ual_color()), size=(1, 1))]]
    window = sg.Window("Reservar lugares", layout, modal=True, text_justification=CENTER, element_justification=CENTER, location=(0,0), size=(600,300), keep_on_top=True).finalize()
    linha +=1
    window.BringToFront()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=='_exit_':
            window.close()
            break