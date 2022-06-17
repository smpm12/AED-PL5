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
                consultar_caixa(lista_reservas, lista_tipo_lugar)
            case "0":
                clear()
                print("Volte sempre\n\n")
                exit()
            case _:
                print("Instrução inválida!!")
                time.sleep(1)




def fazer_reserva(lista_eventos:list, lista_reservas:list, lista_tipo_lugar:list, lista_sala:str):

    clear = lambda: os.system('cls')
    clear() #limpar a consola
    evento_valido: bool = False

    #lista de eventos disponveis
    lista_de_eventos_disponveis = c.verificar_eventos_disponiveis(lista_eventos, lista_reservas)
    print(f"{c.listar_eventos(lista_de_eventos_disponveis)}\n0 - Voltar")

    while not evento_valido:
        
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
                #print(f"{c.get_evento(lista_de_eventos_disponveis, n_evento)}\n")
                #apresentar a sala -  disposição de lugares e lugares livres
                sala.main(lista_sala, lista_reservas_evento, lista_de_eventos_disponveis, n_evento, [], 'M')

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
                                sala.main(lista_sala, lista_reservas_evento, lista_de_eventos_disponveis, n_evento, [], 'M')
                                print(f"\nQuantos lugares pretende reservar?\n")
                                n_lugares = int(input())

                                if not c.verificar_lugares_livres(n_lugares, n_evento, tipo_lugar, lista_reservas_evento):
                                    print(f"Lamentámos mas apenas existem {c.verificar_lugares_livres_tipo(n_evento, tipo_lugar, lista_reservas_evento)} lugares livres para o tipo {c.get_tipo_lugar_descr(tipo_lugar, lista_tipo_lugar)}")
                                else:
                                    lugares_validos = True
                                    lista_lugares = c.sugerir_lugares(n_lugares, tipo_lugar, lista_reservas_evento, lista_sala)
                                    clear()
                                    sala.main(lista_sala, lista_reservas_evento, lista_de_eventos_disponveis, n_evento, lista_lugares, 'M')
                                    
                                    confirmar_lugares_bool:bool = False

                                    print(f"\n\nSugerimos os seguintes lugares:\n{', '.join(lista_lugares)}")
                                    while not confirmar_lugares_bool:
                                        
                                        print(f"\n1 - Confimar Lugares\n2 - Escolher lugares\n\n0 - Cancelar\n")
                                        confirmar_lugares = int(input())

                                        if confirmar_lugares ==0:
                                            #voltar ao menu
                                            confirmar_lugares_bool = True

                                        elif confirmar_lugares == 1:
                                            confirmar_lugares_bool = True
                                            clear()
                                            print(f"Detalhes da reserva:\n\nEvento:\t{c.get_evento(lista_de_eventos_disponveis, n_evento)}\nValor:\t{c.get_valor_reserva(lista_tipo_lugar, tipo_lugar, n_lugares)}€\n")
                                            
                                            nome_cliente:str = ' '
                                            print(f"\nIndique o Nif:")
                                            nif_cliente:str = input()
                                            nif_valido = False
                                            while not nif_valido:
                                                if not c.validar_nif(nif_cliente):
                                                    print("O NIF é inválido\nVerifique o numero e introduza novamente:")
                                                    nif_cliente:str = input()
                                                else:
                                                    nif_valido = True

                                                    if c.criar_reserva(nif_cliente, lista_lugares, n_evento):
                                                        print("Reserva feita com sucesso\n\n")
                                                        time.sleep(2)

                                        elif confirmar_lugares == 2:
                                            confirmar_lugares_bool = True
                                            
                                            lugares_finais_bol = False
                                            while not lugares_finais_bol:
                                                clear()

                                                sala.main(lista_sala, lista_reservas_evento, lista_de_eventos_disponveis, n_evento, [], 'M')
                                                print("Indique os lugares que pretende reservar separados por virgula.\nex:A1,A2\n")

                                                lugares_validos:bool = False
                                                while not lugares_validos:
                                                    
                                                    lugares_reservar:list = input().upper()
                                                    lista_lugares_reservar = [x.strip() for x in lugares_reservar.split(',')]

                                                    lista_lugares_livres = c.get_lista_lugares_livres(n_evento, lista_reservas_evento)
                                                    
                                                    if not c.verificar_lugares(lista_lugares_reservar, lista_lugares_livres):
                                                        
                                                        print("Indicou lugares inválidos, por favor indique os lugares que pretende reservar separados por virgula.\nex:A1,A2\n")
                                                    else:
                                                        lugares_validos = True
                                                        clear()
                                                        sala.main(lista_sala, lista_reservas_evento, lista_de_eventos_disponveis, n_evento, lista_lugares_reservar, 'M')
                                                        confirmar_lugares_pers_bool = False
                                                        while not confirmar_lugares_pers_bool:

                                                            print(f"\n\nReserva:\n{', '.join(lista_lugares_reservar)}")                                            
                                                            print(f"\n1 - Confimar Lugares\n2 - Escolher novos lugares\n\n0 - Cancelar\n")
                                                            confirmar_lugares = int(input())

                                                            if confirmar_lugares ==0:
                                                                confirmar_lugares_pers_bool = True
                                                                lugares_finais_bol = True

                                                            elif confirmar_lugares ==2:
                                                                confirmar_lugares_pers_bool = True

                                                            elif confirmar_lugares == 1:
                                                                confirmar_lugares_pers_bool = True
                                                                lugares_finais_bol = True
                                                                clear()


                                                                confirmar_reserva:bool = False
                                                                while not confirmar_reserva:
                                                                    clear()
                                                                    print(f"Detalhes da reserva:\n\nEvento:\t{c.get_evento(lista_de_eventos_disponveis, n_evento)}\nLugares a reservar: {', '.join(lista_lugares_reservar)}\n\nValor:\t{c.get_valor_operacao(lista_tipo_lugar, lista_lugares_reservar, lista_sala)}€\n")
                                                                    print(f"1 - Confirmar reserva\n2 - Cancelar operação\n")
                                                                    confirmar = input()

                                                                    if confirmar == "1":
                                                                        print(f"\nIndique o Nif:")
                                                                        nif_cliente:str = input()
                                                                        nif_valido = False
                                                                        while not nif_valido:
                                                                            if not c.validar_nif(nif_cliente):
                                                                                print("O NIF é inválido\nVerifique o numero e introduza novamente:")
                                                                                nif_cliente:str = input()
                                                                            else:
                                                                                nif_valido = True

                                                                                if c.criar_reserva(nif_cliente, lista_lugares_reservar, n_evento):
                                                                                    print("Reserva feita com sucesso\n\n")
                                                                                    time.sleep(2)
                                                                                    confirmar_reserva = True
                                                                                    
                                                                                else:
                                                                                    print("Erro - criação de reserva")


                                                                    elif confirmar == "2":
                                                                        print("\nOperação cancelada")
                                                                        time.sleep(2)
                                                                        confirmar_reserva = True
                                                                    else:
                                                                        print("Opção inválida\n\n")
                                                                        time.sleep(1)
                                                            
                                                            else:
                                                                print("Opção inválida")
                                                                
                                        
                                        else:
                                            print("Opção inválida")
                                            




def editar_reserva(lista_eventos:list, lista_reservas:list, lista_tipo_lugar:list, lista_sala:list):
    clear = lambda: os.system('cls')
    clear() #limpar a consola

    
    print("Indique o Nif da pessoa responsável pela reserva:\n")
    nif_cliente:str = input()

    nif_valido = False
    while not nif_valido:
        if not c.validar_nif(nif_cliente):
            print("O NIF é inválido\nVerifique o numero e introduza novamente:")
            nif_cliente:str = input()
        else:
            nif_valido = True

            lista_reservas_cliente = c.get_reservas_cliente(nif_cliente, lista_reservas, lista_eventos)
            if lista_reservas_cliente == []:
                print("Não existem reservas para o Nif indicado")
            else:
                
                lista_de_eventos_disponveis = c.verificar_eventos_com_reserva(lista_reservas_cliente, lista_eventos)

                evento_valido: bool = False
                while not evento_valido:

                    clear()
                    print(f"{c.listar_eventos(lista_de_eventos_disponveis)}\n0 - Voltar")
                    print(f"\nIndique o numero do evento:\n")
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
                            lista_lugares = c.get_lista_lugares(lista_reservas_cliente_eventos)
                            
                            lista_reservas_evento = c.get_lista_reservas_evento(lista_reservas, n_evento)
                            sala.main(lista_sala, lista_reservas_evento, lista_de_eventos_disponveis, n_evento, lista_lugares, 'C')

                            #print(f"{c.listar_lugares(lista_reservas_cliente_eventos, lista_tipo_lugar)}")
                            print("Indique os lugares que pretende remover, caso seja mais do que um, introduza os lugares separados por virgula:\nex:A1,A2\n\nSenão pretender remover lugares pressione a tecla Enter para continuar\n")

                            #remover lugares
                            lugares_validos_remover:bool = False
                            valor_devolucao = 0
                            while not lugares_validos_remover:
                                
                                lugares_remover:list = input().upper()
                                lista_lugares_remover = [x.strip() for x in lugares_remover.split(',')]
                                
                                if lista_lugares_remover[0] == "":
                                    lista_lugares_remover.pop()
                                    lugares_validos_remover = True
                                else:
                                
                                    if not c.verificar_lugares(lista_lugares_remover, lista_reservas_cliente_eventos):
                                        print("Indicou lugares inválidos, por favor indique os lugares que pretende remover")
                                    else:
                                        lugares_validos_remover = True
                                        valor_devolucao = c.get_valor_operacao(lista_tipo_lugar, lista_lugares_remover, lista_sala)


                           
                            clear()

                            lista_lugares = c.atualizar_lista_lugares(lista_lugares, lista_lugares_remover, 'C') 

                            lista_reservas_evento = c.atualizar_lista_reservas_evento(lista_reservas_evento, lista_lugares_remover)
                            sala.main(lista_sala, lista_reservas_evento, lista_de_eventos_disponveis, n_evento, lista_lugares, 'C')

                            #adicionar lugares
                            print("Caso pretenda adicionar lugares a reserva, indique os mesmos separados por virgula.\nex:A1,A2\n\nSenão pretender adicionar lugares pressione a tecla Enter para continuar\n")

                            lugares_validos_marcacao:bool = False
                            valor_marcacao =  0
                            while not lugares_validos_marcacao:
                                
                                lugares_marcacao:list = input().upper()
                                lista_lugares_marcacao = [x.strip() for x in lugares_marcacao.split(',')]

                                if lista_lugares_marcacao[0] == "":
                                    lista_lugares_marcacao.pop()
                                    lugares_validos_marcacao = True
                                else:

                                    if not c.verificar_lugares(lista_lugares_marcacao, lista_reservas_evento):    
                                        print("Indicou lugares inválidos, por favor indique os lugares que pretende reservar separados por virgula ou a tecla Enter para continuar sem adicionar mais lugares.\nex:A1,A2\n")
                                    else:
                                        lugares_validos_marcacao = True
                                        valor_marcacao =  c.get_valor_operacao(lista_tipo_lugar, lista_lugares_marcacao, lista_sala)

                            

                            clear()
                            
                            lista_lugares = c.atualizar_lista_lugares(lista_lugares, lista_lugares_marcacao, 'M') 
                            
                            valor_final = c.verificar_valor_final(valor_devolucao, valor_marcacao)
                            

                            confirmar_alteracao:bool = False
                            while not confirmar_alteracao:
                                clear()
                                sala.main(lista_sala, lista_reservas_evento, lista_de_eventos_disponveis, n_evento, lista_lugares, 'C')
                                print(f"Detalhes da alteração:\n\nEvento:\t{c.get_evento(lista_de_eventos_disponveis, n_evento)}\nLugares_finais:{', '.join(lista_lugares)}\n\n{c.verificar_pagamento(valor_final)}\n")
                                print(f"1 - Confirmar alteração\n2 - Cancelar operação\n")
                                confirmar = input()

                                if confirmar == "1":
                                    
                                    atualizado = False
                                    if len(lista_lugares_remover) > 0:
                                        if c.cancelar_reserva(lista_lugares_remover, nif_cliente, n_evento):
                                            atualizado = True
                                            confirmar_alteracao = True                  
                                        else:
                                            atualizado = False
                                            print("Erro - criação de reserva")
                                    else:
                                        atualizado = True
                                        confirmar_alteracao = True    

                                    if len(lugares_marcacao) > 0:
                                        if c.criar_reserva(nif_cliente, lista_lugares_marcacao, n_evento):
                                            atualizado = True
                                            confirmar_alteracao = True                  
                                        else:
                                            atualizado = False
                                            print("Erro - criação de reserva")
                                    else:
                                        atualizado = True
                                        confirmar_alteracao = True    
                                    
                                    if atualizado == True:
                                        print("\nA operação foi concluida com sucesso")
                                        time.sleep(2)
                                    

                                elif confirmar == "2":
                                    print("\nOperação cancelada")
                                    time.sleep(2)
                                    confirmar_alteracao = True
                                else:
                                    print("Opção inválida\n\n")
                                    time.sleep(1)                               


                                        




def cancelar_reserva(lista_eventos:list, lista_reservas:list, lista_tipo_lugar:list, lista_sala:list):
    clear = lambda: os.system('cls')
    clear() #limpar a consola

    
    print("Indique o Nif da pessoa responsável pela reserva:\n")
    nif_cliente:str = input()

    nif_valido = False
    while not nif_valido:
        if not c.validar_nif(nif_cliente):
            print("O NIF é inválido\nVerifique o numero e introduza novamente:")
            nif_cliente:str = input()
        else:
            nif_valido = True

            lista_reservas_cliente = c.get_reservas_cliente(nif_cliente, lista_reservas, lista_eventos)
            if lista_reservas_cliente == []:
                print("Não existem reservas para o Nif indicado")
                time.sleep(2)
                input()
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
                            lista_lugares = c.get_lista_lugares(lista_reservas_cliente_eventos)
                            
                            lista_reservas_evento = c.get_lista_reservas_evento(lista_reservas, n_evento)
                            sala.main(lista_sala, lista_reservas_evento, lista_de_eventos_disponveis, n_evento, lista_lugares, 'C')

                            #print(f"{c.listar_lugares(lista_reservas_cliente_eventos, lista_tipo_lugar)}")
                            print("Indique as reservas que pretende cancelar, caso seja mais do que uma, introduza os lugares separados por virgula:\nex:A1,A2\n")

                            lugares_validos:bool = False
                            while not lugares_validos:
                                
                                lugares_cancelar:list = input().upper()
                                lista_lugares_cancelar = [x.strip() for x in lugares_cancelar.split(',')]
                                
                                if not c.verificar_lugares(lista_lugares_cancelar, lista_reservas_cliente_eventos):
                                    print("Indicou lugares inválidos, por favor indique os lugares que pretende cancelar")
                                else:
                                    lugares_validos = True

                                    confirmar_cancelamento:bool = False
                                    while not confirmar_cancelamento:
                                        clear()
                                        print(f"Detalhes de cancelamento:\n\nEvento:\t{c.get_evento(lista_de_eventos_disponveis, n_evento)}\nLugares a cancelar: {', '.join(lista_lugares_cancelar)}\n\nValor a rembolsar:\t{c.get_valor_operacao(lista_tipo_lugar, lista_lugares_cancelar, lista_sala)}€\n")
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
                                



def consultar_caixa(lista_reservas:list, lista_tipo_lugar:list):
    clear = lambda: os.system('cls')

    continuar_operacao = True
    while continuar_operacao:
        clear() #limpar a consola
        print("Pretedente consultar o valor em caixa num: \n1 - Dia\n2 - Mes\n3 - Ano\n\n0 - Voltar\n")
        opcao_consultar = input()
        
        opcao_consultar_validar = False
        while not opcao_consultar_validar:
            if opcao_consultar == '1':
                opcao_consultar_validar = True
                print("\nIndique a data que pretende pesquisar (dd-mm-aaaa)")
                data_pesquisa = input()
                valor_caixa = c.pesquisar_caixa(lista_reservas, data_pesquisa, 'D', lista_tipo_lugar)
                

            elif opcao_consultar == '2':
                opcao_consultar_validar = True
                print("\nIndique a data que pretende pesquisar (mm-aaaa)")
                data_pesquisa = input()
                valor_caixa = c.pesquisar_caixa(lista_reservas, data_pesquisa, 'M', lista_tipo_lugar)

            elif opcao_consultar == '3':
                opcao_consultar_validar = True
                print("\nIndique a data que pretende pesquisar (aaaa)")
                data_pesquisa = input()
                valor_caixa = c.pesquisar_caixa(lista_reservas, data_pesquisa, 'A', lista_tipo_lugar)

            elif opcao_consultar == '0':
                opcao_consultar_validar = True
                continuar_operacao = False
                break

            else:
                print("\nOpção inválida\n\n")
                time.sleep(2)
                opcao_consultar_validar = False
                break
            
            print(f"\nO valor da caixa para o periodo {data_pesquisa} é de: {valor_caixa}€")
            print("\n\n1 - Fazer nova consulta\n0 - Voltar")
            
            fazer_nova_pesquisa_bool = False

            while not fazer_nova_pesquisa_bool:
                fazer_nova_pesquisa = input()
            
                if fazer_nova_pesquisa == "1":
                    fazer_nova_pesquisa_bool = True
                elif fazer_nova_pesquisa == "0":
                    fazer_nova_pesquisa_bool = True
                    continuar_operacao = False
                else:
                    print("Opção inválida, insira o numero da operação\n")

        




