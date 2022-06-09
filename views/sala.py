def main_bk(sala_data):
    #sala_data = m.get_sala()
    fila = 1
    fila_old = 0
    fila_print = ''
    print('\n\n    1   2           3   4   5   6   7   8   9   10  11  12      13  14')
    filas = ['','K','J','I','H','G','F',' ','E','D','C','B',' ','A']
    for i in range(len(sala_data)):
        dados = sala_data[i]
        fila = dados[0]
        if dados[4] == 0:
            fila_print = fila_print+'    '
        elif dados[3] == 2:
            fila_print = fila_print+' |V|'
        else:
            fila_print = fila_print+' |_|'            
        if fila > fila_old:
            if fila_old != 0:
                print(filas[fila_old]+' '+fila_print)
            fila_print = ''
        fila_old = fila



def main(lista_sala, lista_reservas):
    
    #sala_data = m.get_sala_livre(2)
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
            print('\033[37m'+filas[fila_old]+' \033[92m'+fila_print)
            fila_print = ''

        if sala[4] == 0:
            fila_print = fila_print+'    '

        elif lugar_reservado:
            fila_print = fila_print+' \033[91m╚X╝'

        elif sala[3] == 2:
            fila_print = fila_print+' \033[92m╚V╝'

        else:
            fila_print = fila_print+' \033[92m╚═╝'           

        fila_old = fila
    print('\033[37m'+filas[fila_old]+' '+fila_print+'\n\n\033[37m')