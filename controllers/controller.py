from models import bdmodel as bd
from datetime import datetime



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
    j:int
    count_lugares_livres:int = 0
    
    for i in range(len(lista_reservas)):
        if lista_reservas[i][0] != evento:
            break
        else:
            if lista_reservas[i][3] == 0 and lista_reservas[i][2] == tipo_lugar:
                count_lugares_livres += 1

    return count_lugares_livres




def sugerir_lugares(n_lugares_reserva:int, tipo_lugar:int, lista_reservas_evento:list, lista_sala:list)->list:
    sugestao:list = []
    ult_fila:int = 0
    fila_atual:int = 0
    i:int
    j:int

    #sugestão de lugares seguidos
    for i in range(len(lista_reservas_evento)):
        if not(lista_reservas_evento[i][3] == 0 and lista_reservas_evento[i][2] == tipo_lugar):
            break
        else:
            for j in range(len(lista_sala)):
                if lista_sala[j][2] == lista_reservas_evento[i][1]:
                    fila_atual = lista_sala[j][0]
                    break
            if fila_atual == ult_fila:
                sugestao.append(lista_reservas_evento[i][1])
            else:
                sugestao.clear()

        ult_fila = fila_atual

        if len(sugestao) == n_lugares_reserva:
            break
    
    #se não encontramos os lugares todos seguidos, limpamos a lista e tentamos a segunda hipotese
    if len(sugestao) < n_lugares_reserva:
        sugestao.clear()


    #sugestão separada, caso não existam lugares seguidos
    if sugestao == []:
        for i in range(len(lista_reservas_evento)):
            if lista_reservas_evento[i][3] == 0 and lista_reservas_evento[i][2] == tipo_lugar:
                sugestao.append(lista_reservas_evento[i][1])

            if len(sugestao) == n_lugares_reserva:
                break
    
    return sugestao




def get_valor_bilhete(lista_tipo_lugar:list, tipo_lugar:int)->float:
    i:int
    for i in range (len(lista_tipo_lugar)):
        if tipo_lugar == lista_tipo_lugar[i][0]:
            return lista_tipo_lugar[i][2]




def get_valor_reserva(lista_tipo_lugar:list, tipo_lugar:str, n_lugares:int)->float:
    return get_valor_bilhete(lista_tipo_lugar, tipo_lugar) * n_lugares
    



def get_valor_devolucao(lista_tipo_lugar:list, lista_lugares_cancelar:list, lista_reservas_cliente_eventos:list)->int:
    i:int
    valor_devolucao:float = 0 
    for lugar in lista_lugares_cancelar:
        for i in range(len(lista_reservas_cliente_eventos)):
            if lista_reservas_cliente_eventos[i][1] == lugar:
                valor_devolucao = valor_devolucao + get_valor_bilhete(lista_tipo_lugar, lista_reservas_cliente_eventos[i][2])
    
    return valor_devolucao




def criar_reserva(nome_cliente:str, nif_cliente:str, lista_lugares:list, n_evento:int) -> bool:
    i:int
    for i in range(len(lista_lugares)):
        if i == 0:
            lugares = f"'{lista_lugares[i]}'"
        else:
            lugares:str = f"{lugares}, '{lista_lugares[i]}'"
    return bd.criar_reserva(nif_cliente, n_evento, lugares)




def get_reservas_cliente(nif_cliente:str, lista_reservas:list)->list:
    
    i:int
    lista_reservas_cliente:list = []
    for i in range(len(lista_reservas)):
        if lista_reservas[i][4] == nif_cliente:
            lista_reservas_cliente.append(lista_reservas[i])

    return lista_reservas_cliente




def get_lista_reservas_cliente_eventos(reservas_cliente:list, n_evento:int)-> list:
    i:int
    lista_reservas_cliente_eventos:list = []
    for i in range (len(reservas_cliente)):
        if reservas_cliente[i][0] == n_evento:
            lista_reservas_cliente_eventos.append(reservas_cliente[i])

    return lista_reservas_cliente_eventos




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