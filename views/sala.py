from controllers import controller as c


def main(lista_sala, lista_reservas, lista_de_eventos_disponveis, n_evento, lista_lugares_sugeridos):
    print(f"{c.get_evento(lista_de_eventos_disponveis, n_evento)}\n")
    
    fila = 1
    fila_old = 1
    fila_print = ''
    print('\n\n    1   2           3   4   5   6   7   8   9  10  11  12      13  14')
    filas = ['','K','J','I','H','G','F',' ','E','D','C','B',' ','A']
    for i in range(len(lista_sala)):
        sala = lista_sala[i]

        lugar_reservado:bool = False
        for reserva in lista_reservas:
            if reserva[1] == sala[2] and reserva[3] == 1:
                lugar_reservado = True
                break

        fila = sala[0]

        if fila > fila_old:
            #if fila_old != 0:
            #print('\033[37m'+filas[fila_old]+' \033[92m'+fila_print)
            print('\033[37m'+filas[fila_old]+' '+fila_print)
            fila_print = ''

        escolhido = False

        for lugar in lista_lugares_sugeridos:
            if lugar == sala[2]:
                fila_print = fila_print+' \033[92m╚X╝\033[37m'
                escolhido = True
                break

        if sala[4] == 0:
            fila_print = fila_print+'    '

        elif lugar_reservado and not escolhido:
            fila_print = fila_print+' \033[91m╚X╝\033[37m'

        elif sala[3] == 2 and not escolhido:
            #fila_print = fila_print+' \033[92m╚V╝'
            fila_print = fila_print+' ╚V╝'

        elif not escolhido:
            #fila_print = fila_print+' \033[92m╚═╝'
            fila_print = fila_print+' ╚═╝'

        fila_old = fila
    
    print('\033[37m'+filas[fila_old]+' '+fila_print+'\n\n\033[37m')
    print('\t ____________________________________________________________')
    print('\t|                                                            |')
    print('\t|                         PALCO                              |')
    print('\t|                                                            |')

    print('\n\n\033[37m╚═╝ - Lugar Normal disponivel\t\t\033[91m╚X╝\033[37m - Lugar Ocupado')
    print('\033[37m╚V╝\033[37m - Lugar VIP disponivel\t\t\033[92m╚X╝\033[37m - Lugar Escolhido\n\n')