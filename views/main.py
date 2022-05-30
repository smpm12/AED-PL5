import PySimpleGUI as sg
from views import windows as w
from controllers import controller as c

# Main Window
def main():

    #argumentos para o nivel 0
    args:list = ['Homepage', (0,0)]

    #argumentos para o nivel 1
    args1:list = []

    #argumentos para o nivel 2
    args2:list = []


    window_location:tuple

#nivel 0 - homepage
    window = w.create_window(args)
    #window.Maximize()


#criar uma window2 com modal para as prompts (exemplo: confirmar reserva/cancelamentos)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        #nivel 1 - Eventos
        if event == 'Fazer Reserva':
            args1 = []
            window_location= window.CurrentLocation()
            args1.append('Eventos')
            args1.append(window_location)
            window.close()
            window = w.create_window(args1)
        
        #nivel 1
        if event in c.listar_eventos():
            args2 = []
            args2.append('Sala')
            window_location= window.CurrentLocation()
            args2.append(window_location)
            args2.append(event)
            window.close()
            window = w.create_window(args2)

        #nivel 2
        if event == 'Voltar':
            if args2 != []:
                window.close()
                window = w.create_window(args1)
            else:
                if args1 != []:
                    window.close()
                    window = w.create_window(args)
            
                
                


       