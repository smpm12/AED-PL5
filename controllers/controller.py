from models import bdmodel as bd



def listar_eventos():

    lista_eventos:list = []
    eventos = bd.get_eventos()
    lista_eventos:str = ""
    for id, evento, data in eventos:
        while len(evento) < 45:
            evento = f"{evento} "

        lista_eventos:str = f"{lista_eventos}{id} - {evento}\t{data}\n"

    return lista_eventos


def verificar_lugares_livres()->True:
    return True



def sugerir_lugares(n_evento:int, n_lugares_reserva:int, tipo_lugar:str):
    lugares = bd.get_sala_livre(n_evento)
    sugestao:list = []
    is_vip = 0
    if tipo_lugar == "V":
        
        is_vip =1

    #sugestão de lugares seguidos
    for lugar, vip, ativo, estado in lugares:
        if ativo == 1 and estado == 0 and vip == is_vip:
            sugestao.append(lugar)
        else:
            sugestao.clear()
        
        if len(sugestao) == n_lugares_reserva:
            break

    #sugestão separada, caso não existam lugares seguidos
    if sugestao == []:
        for lugar, vip, ativo, estado in lugares:
            if ativo == 1 and estado == 0 and vip == is_vip:
                sugestao.append(lugar)

            if len(sugestao) == n_lugares_reserva:
                break

    return sugestao

