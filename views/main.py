import time
from controllers import controller as c
from views import sala 
import os

def view():

    clear = lambda: os.system('cls')
    lista_eventos = c.get_lista_eventos()
    
    lista_tipo_lugar = c.get_lista_tipo_lugar()
    lista_sala = c.get_lista_sala()


    while True:
        clear()
        lista_reservas = c.get_lista_reservas()
        print("Sala de Eventos\n\n1-Fazer Reserva\n2-Editar Reserva\n3-Cancelar Reserva\n4-Consultar Caixa\n\n0 - Sair\n\n")
        menu:str = input()
        match menu:
            case "1":
                fazer_reserva(lista_eventos, lista_reservas, lista_tipo_lugar, lista_sala)
            case "2":
                editar_reserva(lista_eventos, lista_reservas, lista_tipo_lugar, lista_sala)
            case "3":
                cancelar_reserva(lista_eventos, lista_reservas, lista_tipo_lugar, lista_sala)
            case "4":
                consultar_caixa()
            case "0":
                clear()
                print("Volte sempre\n\n")
                exit()
            case _:
                print("Instrução inválida!!")




def fazer_reserva(lista_eventos:list, lista_reservas:list, lista_tipo_lugar:list, lista_sala:str):

    clear = lambda: os.system('cls')
    clear() #limpar a consola
    evento_valido: bool = False

    #lista de eventos disponveis
    lista_de_eventos_disponveis = c.verificar_eventos_disponiveis(lista_eventos, lista_reservas)
    while not evento_valido:

        print(f"{c.listar_eventos(lista_de_eventos_disponveis)}\n0 - Voltar")
        print(f"\nIndique o numero do evento que deseja reservar:\n")

        n_evento:int = int(input())

        if n_evento == 0:
            #voltar ao menu
            evento_valido = True
        else:

            #verificar se o numero introduzido corresponde a um evento
            if not c.verificar_input(lista_de_eventos_disponveis, n_evento):
                print(f"Opção inválida")
                evento_valido = False
            else:
                evento_valido = True
                clear()
                lista_reservas_evento = c.get_lista_reservas_evento(lista_reservas, n_evento) 
                print(f"{c.get_evento(lista_de_eventos_disponveis, n_evento)}\n")
                #apresentar a sala -  disposição de lugares e lugares livres
                sala.main(lista_sala, lista_reservas)

                #escolher tipo de lugar
                tipo_lugar_valido:bool = False

                while not tipo_lugar_valido:
                    print(f"\n{c.listar_tipo_lugar(lista_tipo_lugar)}\n0 - Voltar\n")
                    
                    tipo_lugar = int(input())
                    
                    if tipo_lugar == 0:
                        #voltar ao menu
                        tipo_lugar_valido = True
                    else:

                        if not c.verificar_input(lista_tipo_lugar, tipo_lugar):
                            print(f"Opção inválida, indique o tipo de lugar pretendido")
                        else:
                            tipo_lugar_valido = True

                            lugares_validos:bool = False
                            while not lugares_validos:
                                clear()
                                sala.main(lista_sala, lista_reservas)
                                print(f"\nQuantos lugares pretende reservar?\n")
                                n_lugares = int(input())

                                if not c.verificar_lugares_livres(n_lugares, n_evento, tipo_lugar, lista_reservas_evento):
                                    print(f"Lamentámos mas apenas existem {c.verificar_lugares_livres_tipo(n_evento, tipo_lugar, lista_reservas_evento)} lugares livres para o tipo {c.get_tipo_lugar_descr(tipo_lugar, lista_tipo_lugar)}")
                                else:
                                    lugares_validos = True
                                    lista_lugares = c.sugerir_lugares(n_lugares, tipo_lugar, lista_reservas_evento, lista_sala)
                                    clear()
                                    print(lista_lugares)
                                    sala.main(lista_sala, lista_reservas)
                                    
                                    confirmar_lugares:bool = False

                                    while not confirmar_lugares:
                                        print(f"\n\nSugerimos os seguintes lugares:\n{', '.join(lista_lugares)}")
                                        print(f"\n1 - Confimar Lugares\n2 - Escolher lugares\n\n0 - Cancelar\n")
                                        confirmar_lugares = int(input())

                                        if confirmar_lugares ==0:
                                            #voltar ao menu
                                            confirmar_lugares = True

                                        elif confirmar_lugares == 1:
                                            confirmar_lugares = True
                                            clear()
                                            print(f"Detalhes da reserva:\n\nEvento:\t{c.get_evento(lista_de_eventos_disponveis, n_evento)}\nValor:\t{c.get_valor_reserva(lista_tipo_lugar, tipo_lugar, n_lugares)}€\n")
                                            print(f"\nIndique o nome em que a reserva fica:")
                                            nome_cliente:str = input()
                                            print(f"\nIndique o Nif:")
                                            nif_cliente:str = input()

                                            if c.criar_reserva(nome_cliente, nif_cliente, lista_lugares, n_evento):
                                                print("Reserva feita com sucesso\n\n")
                                                time.sleep(2)

                                        elif confirmar_lugares == 2:
                                            confirmar_lugares = True
                                        
                                        else:
                                            print("Opção inválida")
                                            




def editar_reserva():
    pass




def cancelar_reserva(lista_eventos:list, lista_reservas:list, lista_tipo_lugar:list, lista_sala:list):
    clear = lambda: os.system('cls')
    clear() #limpar a consola

    
    print("Indique o Nif da pessoa responsável pela reserva:\n")
    nif_cliente:str = input()

    lista_reservas_cliente = c.get_reservas_cliente(nif_cliente, lista_reservas)
    if lista_reservas_cliente == []:
        print("Não existem reservas para o Nif indicado")
    else:
        
        lista_de_eventos_disponveis = c.verificar_eventos_com_reserva(lista_reservas_cliente, lista_eventos)

        evento_valido: bool = False
        while not evento_valido:

            clear()
            print(f"{c.listar_eventos(lista_de_eventos_disponveis)}\n0 - Voltar")
            print(f"\nIndique o numero do evento que deseja cancelar:\n")
            n_evento:int = int(input())

            if n_evento == 0:
                #voltar ao menu
                evento_valido = True
            else:

                #verificar se o numero introduzido corresponde a um evento
                if not c.verificar_input(lista_de_eventos_disponveis, n_evento):
                    print(f"Opção inválida")
                    evento_valido = False
                else:
                    evento_valido = True
                    clear()
                    lista_reservas_cliente_eventos = c.get_lista_reservas_cliente_eventos(lista_reservas_cliente, n_evento)
                    
                    print(f"{c.listar_lugares(lista_reservas_cliente_eventos, lista_tipo_lugar)}")
                    print("Indique as reservas que pretende cancelar, caso seja mais do que uma, introduza os lugares separados por virgula:\nex:A1,A2\n")

                    lugares_validos:bool = False
                    while not lugares_validos:
                        
                        lista_lugares_cancelar:list = input().split(",")
                        
                        if not c.verificar_lugares(lista_lugares_cancelar, lista_reservas_cliente_eventos):
                            print("Indicou lugares inválidos, por favor indique os lugares que pretende cancelar")
                        else:
                            lugares_validos = True

                            confirmar_cancelamento:bool = False
                            while not confirmar_cancelamento:
                                clear()
                                print(f"Detalhes de cancelamento:\n\nEvento:\t{c.get_evento(lista_de_eventos_disponveis, n_evento)}\nValor:\t{c.get_valor_devolucao(lista_tipo_lugar, lista_lugares_cancelar, lista_reservas_cliente_eventos)}€\n")
                                print(f"1 - Confirmar cancelamento\n2 - Cancelar operação\n")
                                confirmar = input()

                                if confirmar == "1":
                                    if c.cancelar_reserva(lista_lugares_cancelar, nif_cliente, n_evento):
                                        print("\nA reserva foi cancelada, o montante foi reembolsado")
                                        time.sleep(2)
                                        confirmar_cancelamento = True
                                    else:
                                        print("Erro - cancelamento de reserva")
                                elif confirmar == "2":
                                    print("\nOperação cancelada")
                                    time.sleep(2)
                                    confirmar_cancelamento = True
                                else:
                                    clear()
                                    print("Opção inválida\n\n")
                                




            




    



def consultar_caixa():
    pass