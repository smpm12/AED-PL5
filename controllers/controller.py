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
    sala_evento:list = []
    sla = bd.get_eventos()
