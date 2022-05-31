import models.bdmodel as m
import controllers.controller as c

def main():
    sala_data = m.get_sala()
    fila = 1
    fila_old = 0
    fila_print = ''
    print('\n\n    1   2           3   4   5   6   7   8   9   10  11  12      13  14')
    filas = ['','K','J','I','H','G','F',' ','E','D','C','B',' ','A']
    for i in range(len(sala_data)):
        dados = sala_data[i]
        fila = dados[1]
        if dados[5] == 0:
            fila_print = fila_print+'    '
        elif dados[4] == 1:
            fila_print = fila_print+' |V|'
        else:
            fila_print = fila_print+' |_|'            
        if fila > fila_old:
            if fila_old != 0:
                print(filas[fila_old]+' '+fila_print)
            fila_print = ''
        fila_old = fila

