from models import bdmodel as bd
import PySimpleGUI as sg

def criar_botoes_eventos():

    botoes_eventos:list = []
    eventos = bd.get_eventos()
    botoes_eventos = [
        [sg.Button( evento[0], font = 'Franklin 14',size = (15,3),pad = (40,20))] for evento in eventos 
        ]

    return botoes_eventos


def listar_eventos():

    lista_eventos:list = []
    eventos = bd.get_eventos()
    for evento in eventos:
        lista_eventos.append(evento[0])

    return lista_eventos


def criar_sala():
    lugares_fila = []
    n_colunas = bd.get_sala_n_coluna()
    n_filas = bd.get_sala_n_filas()
    sala_dataset = bd.get_sala()
    lugares = [[]]
    for i in range (n_filas):
        for j in range(n_colunas):
            lugares_fila.append(sala_dataset[(i*n_colunas)+j][3])

        lugares.append(            
                [sg.Button(lugar, font = 'Franklin 14',size = (1,1),pad = (2,2))] for lugar in lugares_fila 
            )
        lugares_fila = []

    return lugares
   
        
