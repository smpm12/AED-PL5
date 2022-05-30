import PySimpleGUI as sg
from controllers import controller as c

def create_window(args:list):

    match args[0]:
        case "Homepage":
            sg.theme('LightGrey1')
            sg.set_options(font = 'Franklin 14', button_element_size= (6,3))

            layout = [
                [sg.Push(),sg.Button(
                    'Login', 
                    font = 'Franklin 8',
                    button_color= 'DarkGrey',
                    size = (10,1)
                    )
                ],
                [sg.Text(
                    'Sala de espetáculos', 
                    font = 'Franklin 30', 
                    justification= 'center', 
                    expand_x= True, 
                    background_color = None,
                    pad = (10,20),
                    key = '-HEADER-'
                    )
                ],
                [sg.Button(
                    'Fazer Reserva', 
                    font = 'Franklin 14',
                    size = (15,3)
                    )
                ],
                [sg.Button(
                    'Cancelar Reserva', 
                    font = 'Franklin 14',
                    size = (15,3)
                    )
                ],
                [sg.Button(
                    'Alterar Reserva', 
                    font = 'Franklin 14',
                    size = (15,3)
                    )
                ]

            ]
            return sg.Window('AED - Sala de espetáculos', layout, resizable=True, size=(800,600), element_justification='c').finalize()


        case "Eventos":
            sg.theme('LightGrey1')
            sg.set_options(font = 'Franklin 14', button_element_size= (6,3))

            botoes_eventos = c.criar_botoes_eventos()

            layout = [
                [sg.Button(
                    'Voltar', 
                    font = 'Franklin 10',
                    button_color= 'Red',
                    size = (10,1)
                    )
                ],
                [sg.Text(
                    'Eventos', 
                    font = 'Franklin 30', 
                    justification= 'center', 
                    expand_x= True, 
                    background_color = None,
                    pad = (10,20),
                    key = '-HEADER-'
                    )
                ],
                [sg.Column(botoes_eventos, scrollable=True, vertical_scroll_only= True, justification = 'left', element_justification = 'center', expand_y = True, pad= (10,20))]
            ]
            return sg.Window('Eventos', layout, resizable=True, location= args[1], size=(800,600)).finalize()


        case "Sala":
            sg.theme('LightGrey1')
            sg.set_options(font = 'Franklin 14', button_element_size= (6,3))

            lugares =c.criar_sala()

            layout = [
                [sg.Button(
                    'Voltar', 
                    font = 'Franklin 10',
                    button_color= 'Red',
                    size = (10,1)
                    )
                ],
                [sg.Text(
                    args[2], 
                    font = 'Franklin 30', 
                    justification= 'center', 
                    expand_x= True, 
                    background_color = None,
                    pad = (10,20),
                    key = '-HEADER-'
                    )
                ],
                lugares
            ]
            return sg.Window('Eespetáculos', layout, resizable=True, location= args[1], size=(800,600)).finalize()