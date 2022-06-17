from models import bdmodel as bd
from datetime import datetime
from operator import itemgetter


def get_lista_eventos()->list:
    return bd.get_eventos()


def get_lista_reservas()->list:
    return bd.get_reservas()


def get_lista_tipo_lugar()->list:
    return bd.get_tipos_lugares()


def get_lista_sala()->list:
    return bd.get_sala()




def verificar_eventos_disponiveis(lista_eventos:list, lista_reservas:list)-> list:
    lista_eventos_disponveis:list = []
    i:int
    j:int
    for i in range (len(lista_eventos)):
        if lista_eventos[i][2] < datetime.now():
            break
        else:
            for j in range(len(lista_reservas)):
                if lista_reservas[j][0] == lista_eventos[i][0] and lista_reservas[j][3] == 0:
                    lista_eventos_disponveis.append(lista_eventos[i])
                    break
    
    return lista_eventos_disponveis
          



def verificar_eventos_com_reserva(lista_reservas_cliente:list, lista_eventos:list) ->list:

    lista_eventos_disponveis:list = []
    i:int
    j:int
    for i in range (len(lista_eventos)):
        
        for j in range(len(lista_reservas_cliente)):
            if lista_reservas_cliente[j][0] == lista_eventos[i][0]:
                #não podem ser cancelados eventos no proprio dia, só para datas futuras
                if lista_eventos[i][2] > datetime.now():
                    lista_eventos_disponveis.append(lista_eventos[i])
                    break
    
    return lista_eventos_disponveis




def listar_eventos(lista_eventos:list):

    str_eventos:str = ""
    for id, evento, data in lista_eventos:
        while len(evento) < 45:
            evento = f"{evento} "

        str_eventos:str = f"{str_eventos}{id} - {evento}\t{data}\n"

    return str_eventos
    



def verificar_input(lista_opcoes:list, opcao:int):
    i:int
    for i in range(len(lista_opcoes)):
        if opcao == lista_opcoes[i][0]:
            return True
    return False




def get_evento(lista_eventos:list, n_evento:int):

     for id, evento, data in lista_eventos:
        if n_evento == id:
            return f"{evento}___{data}"




def listar_tipo_lugar(tipo_lugares):
    str_tipo_lugares:str = ""
    for id, tipo, preco in tipo_lugares:
        while len(tipo) < 10:
            tipo = f"{tipo}_"

        str_tipo_lugares:str = f"{str_tipo_lugares}{id} - {tipo}__{preco}€\n"

    return str_tipo_lugares




def get_lista_reservas_evento(lista_reservas:list, n_evento:int)->list:
    i:int
    lista_reservas_evento:list = []
    for i in range(len(lista_reservas)):
        if lista_reservas[i][0] == n_evento:
            lista_reservas_evento.append(lista_reservas[i])
    
    return lista_reservas_evento




def verificar_lugares_livres(n_lugares_pedido:int, evento:int, tipo_lugar:int, lista_reservas:list)-> bool:

    if verificar_lugares_livres_tipo(evento, tipo_lugar, lista_reservas) < n_lugares_pedido:
        return False
    else:
        return True




def get_tipo_lugar_descr(tipo_lugar:int, lista_tipo_lugar:list):
    
    i:int
    for i in range(len(lista_tipo_lugar)):
        if tipo_lugar == lista_tipo_lugar[i][0]:
            return lista_tipo_lugar[i][1]




def verificar_lugares_livres_tipo(evento:int, tipo_lugar:int, lista_reservas:list)->int:
    i:int
    count_lugares_livres:int = 0
    
    for i in range(len(lista_reservas)):
        if lista_reservas[i][0] != evento:
            break
        else:
            if lista_reservas[i][3] == 0 and lista_reservas[i][2] == tipo_lugar:
                count_lugares_livres += 1

    return count_lugares_livres




def get_lista_lugares_livres(evento:int, lista_reservas:list)-> list:
    i:int
    lista_lugares_livres:list = []
    
    for i in range(len(lista_reservas)):
        if lista_reservas[i][0] != evento:
            break
        else:
            if lista_reservas[i][3] == 0:
                lista_lugares_livres.append(lista_reservas[i])

    return lista_lugares_livres




def sugerir_lugares(n_lugares_reserva:int, tipo_lugar:int, lista_reservas_evento:list, lista_sala:list)->list:
    sugestao:list = []
    ult_fila:int = 0
    fila_atual:int = 0
    
    lista_sala.reverse()
    #sugestão de lugares seguidos
    for lugar_sala in lista_sala:
        if lugar_sala[4] == 0:
            sugestao.clear()
        else:
            for lugar in lista_reservas_evento:
                if lugar_sala[2] == lugar[1]:
                    if not(lugar[3] == 0 and lugar[2] == tipo_lugar):
                        sugestao.clear()
                
                    else:
                        fila_atual = lugar_sala[0]
                        if fila_atual == ult_fila or len(sugestao) == 0:
                            sugestao.append(lugar[1])
                
                        else:
                            sugestao.clear()
                        ult_fila = fila_atual
                    break

        if len(sugestao) == n_lugares_reserva:
            break


    
    #se não encontramos os lugares todos seguidos, limpamos a lista e tentamos a segunda hipotese
    if len(sugestao) < n_lugares_reserva:
        sugestao.clear()


    #sugestão separada, caso não existam lugares seguidos
    if sugestao == []:
        for lugar in lista_reservas_evento:
            if lugar[3] == 0 and lugar[2] == tipo_lugar:
                sugestao.append(lugar[1])

            if len(sugestao) == n_lugares_reserva:
                break
    
    lista_sala.reverse()
    return sugestao




def get_valor_bilhete(lista_tipo_lugar:list, tipo_lugar:int)->float:
    i:int
    for i in range (len(lista_tipo_lugar)):
        if tipo_lugar == lista_tipo_lugar[i][0]:
            return lista_tipo_lugar[i][2]




def get_valor_reserva(lista_tipo_lugar:list, tipo_lugar:str, n_lugares:int)->float:
    return get_valor_bilhete(lista_tipo_lugar, tipo_lugar) * n_lugares
    



def get_valor_operacao(lista_tipo_lugar:list, lista_lugares_operacao:list, lista_sala:list)->int:
    i:int
    valor_operacao:float = 0 
    for lugar in lista_lugares_operacao:
        for lugar_sala in lista_sala:
            if lugar_sala[2] == lugar:
                valor_operacao = valor_operacao + get_valor_bilhete(lista_tipo_lugar, lugar_sala[3])
    
    return valor_operacao




def criar_reserva(nif_cliente:str, lista_lugares:list, n_evento:int) -> bool:
    i:int
    for i in range(len(lista_lugares)):
        if i == 0:
            lugares = f"'{lista_lugares[i]}'"
        else:
            lugares:str = f"{lugares}, '{lista_lugares[i]}'"
    return bd.criar_reserva(nif_cliente, n_evento, lugares)




def get_reservas_cliente(nif_cliente:str, lista_reservas:list, lista_eventos:list)->list:
    
    i:int
    lista_reservas_cliente:list = []
    for evento in lista_eventos:
        if evento[2] > datetime.now():
            for reserva in lista_reservas:
                if reserva[0] == evento[0]:
                    if reserva[4] == nif_cliente:
                        lista_reservas_cliente.append(reserva)




    return lista_reservas_cliente




def get_lista_reservas_cliente_eventos(reservas_cliente:list, n_evento:int)-> list:
    i:int
    lista_reservas_cliente_eventos:list = []
    for i in range (len(reservas_cliente)):
        if reservas_cliente[i][0] == n_evento:
            lista_reservas_cliente_eventos.append(reservas_cliente[i])

    return lista_reservas_cliente_eventos




def get_lista_lugares(lista_reservas_cliente_eventos:list)-> list:
    lista_lugares:list = []
    for lugar in lista_reservas_cliente_eventos:
        lista_lugares.append(lugar[1])
    
    return lista_lugares







def listar_lugares(lista_reservas_cliente_eventos, lista_tipo_lugar)->str:
    str_lugares:str = ""
    i:int
    j:int
    for i in range(len(lista_reservas_cliente_eventos)):
            str_lugares:str = f"{str_lugares}{lista_reservas_cliente_eventos[i][1]} - {get_tipo_lugar_descr(lista_reservas_cliente_eventos[i][2],lista_tipo_lugar, )}\n"

    return str_lugares




def verificar_lugares(lista_lugares_cancelar:list, lista_reservas:list)->bool:
    for lugar in lista_lugares_cancelar:
        exists:bool = False
        for i in range(len(lista_reservas)):
            if lugar == lista_reservas[i][1]:
                exists = True
                break
        if exists == False:
            return False
    return True




def cancelar_reserva(lista_lugares_cancelar:list, nif_cliente:str, n_evento:int)->list:
    i:int
    for i in range(len(lista_lugares_cancelar)):
        if i == 0:
            lugares = f"'{lista_lugares_cancelar[i]}'"
        else:
            lugares:str = f"{lugares}, '{lista_lugares_cancelar[i]}'"
    return bd.cancelar_reserva(nif_cliente, n_evento, lugares)




def pesquisar_caixa(lista_reservas:list, data_pesquisa:str, periodo:str, lista_tipo_lugar:str)-> float:
    reservas:list

    total:float = 0

    if periodo == 'D':
        formato_data = "%d-%m-%Y"
    if periodo == 'M':
        formato_data = "%m-%Y"
    if periodo == 'A':
        formato_data = "%Y"


    for reservas in lista_reservas:
        if reservas[3] == 1:
            if reservas[5].strftime(formato_data) == data_pesquisa:
                for tipo in lista_tipo_lugar:
                    if reservas[2] == tipo[0]:
                        total = total + tipo[2]
                        break
                

    return total




def validar_nif (nif_cliente):
    if len(nif_cliente) != 9:
        return False
    
    for digito in nif_cliente:
        if not digito.isnumeric():
            return False
    
    return True




def atualizar_lista_lugares(lista_lugares, lista_lugares_operacao, operacao):
    
    
    for lugar in lista_lugares_operacao:
        if operacao == 'C':
            lista_lugares.remove(lugar)
        elif operacao == 'M':
            lista_lugares.append(lugar)


    return lista_lugares




def atualizar_lista_reservas_evento(lista_reservas_evento, lista_lugares_remover):
    i:int

    for lugar in lista_lugares_remover:
        for i in range(len(lista_reservas_evento)):
            if lista_reservas_evento[i][1] == lugar:
                lista_reservas_evento[i] = [lista_reservas_evento[i][0],lista_reservas_evento[i][1],lista_reservas_evento[i][2], 0, None, None]

    return lista_reservas_evento




def verificar_valor_final(valor_devolucao, valor_marcacao):
    return valor_marcacao - valor_devolucao




def verificar_pagamento(valor_final):
    if valor_final < 0:
        return f"Valor a rembolsar: {valor_final * -1}€"
    elif valor_final > 0:
        return f"Valor a pagar: {valor_final}€"
    elif valor_final == 0:
        return f"Sem custos de alteração"


