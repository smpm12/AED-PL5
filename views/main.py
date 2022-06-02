from controllers import controller as c
#import model as m
import os

def view():

    clear = lambda: os.system('cls')
    while True:
        clear()
        print("Sala de Eventos\n\n1-Fazer Reserva\n2-Editar Reserva\n3-Cancelar Reserva\n4-Consultar Caixa")
        
        menu:str = input()
        match menu:
            case "1":

                clear()
                #listar apenas espetaculos com lugares livres
                print(c.listar_eventos())
                print(f"\nIndique o numero corresponder ao evento que deseja reservar:")
                n_evento:int = int(input())

                if c.verificar_lugares_livres():
                    clear()
                    print(f"Tipo de Lugar:\nN-Normal\nV-VIP")
                    tipo_lugar = input()
                    print(f"\nQuantos lugares deseja reservar?")
                    #verificar se existem x lugares seguidos , conforme a reservva, senão sugere separadamente
                    lugares_input:str = int(input())
                    print(c.sugerir_lugares(n_evento, lugares_input, tipo_lugar))
                    input()



            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case _:
                print("Instrução inválida!!")


