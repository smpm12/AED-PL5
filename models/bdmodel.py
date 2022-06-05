#from mysql.connector import connect as c, Error
import mysql.connector
from mysql.connector import Error


def connect_bd():
    try:
        connection = mysql.connector.connect(host='ual-pl05.cqjer8kzbahe.eu-west-3.rds.amazonaws.com',
                            port='3306',
                            database='ual-pl05',
                            user='admin',
                            password='ual-pl05')
                            
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
    

def get_eventos(): 
    #comando:str = f"Select id, Nome, Data from `ual-pl05`.Eventos where data >= sysdate()"
    #apenas eventos disponiveis
    #data >= que hoje e com lugares livres
    #comando:str = f"Select e.id_evento, e.nome, e.data from sala_eventos.eventos e where data >= sysdate() and exists (Select 'x' from sala_eventos.reservas r where r.id_evento = e.id_evento having count(*) > 0)"
    comando:str = f"Select e.id_evento, e.nome, e.data from sala_eventos.eventos e"
    return run_query(comando)
   

def get_reservas():
    comando:str = f"select id_evento, lugar, id_tipo, id_estado, id_cliente, data_reserva from sala_eventos.reservas"
    return run_query(comando)



def get_tipos_lugares():
    comando:str = f"Select id_tipo, tipo, preco from sala_eventos.tipo_lugar"
    return run_query(comando)




def get_sala():
    #comando:str = f"SELECT id, Fila, Coluna, Lugar, Vip, Ativo, Preco FROM `ual-pl05`.Sala"
    comando:str = f"SELECT Fila, Coluna, Lugar, id_tipo, Ativo FROM sala_eventos.sala"
    return run_query(comando)
      


#def get_sala_livre(evento:int):
#    #comando:str = f"Select s.lugar, s.VIP, s.Ativo, r.estadoid from `ual-pl05`.Sala s left join `ual-pl05`.Reservas r on r.SalaId = s.id and r.EventoId = {evento} order by fila desc, coluna asc"
#    comando:str = f"Select r.lugar, s.id_tipo, s.Ativo, r.id_estado from sala_eventos.reservas r left join sala_eventos.sala s on r.id_lugar = s.lugar and r.id_evento = 1 order by fila desc, coluna asc"
#    return run_query(comando)
        

#def get_lugares_livres_evento(evento:int, tipo_lugar:str):
#    #comando:str = f"Select count(*) from `ual-pl05`.Reservas where EventoId = {evento} and estadoid = 0"
#    #comando:str = f"Select count(r.SalaId) from `ual-pl05`.Reservas r left join `ual-pl05`.Sala s on r.SalaId = s.id where r.EventoId = {evento} and r.estadoid = 0 and (s.VIP = {is_vip} or {is_vip} = 9)"
#    comando:str = f"Select count(*) from sala_eventos.reservas r left join sala_eventos.sala s on r.id_lugar = s.lugar where r.id_evento = {evento} and r.id_estado = 0 and s.id_tipo = '{tipo_lugar}'"
#    
#    return run_query(comando)[0][0]



def criar_reserva(nif:str, evento:int, lugares:str):
    comando:str = f"update sala_eventos.reservas set id_estado = 1, id_cliente = {nif}, data_reserva = sysdate() where id_evento = {evento} and lugar in ({lugares})"
    return run_and_commit_query(comando)


def cancelar_reserva(nif:str, evento:int, lugares:str ):
    comando:str = f"update sala_eventos.reservas set id_estado = 0, id_cliente = null, data_reserva = null where id_evento = {evento} and lugar in ({lugares})"
    return run_and_commit_query(comando)


#def get_reservas_cliente(nif_cliente:str):
#    comando:str = f"Select id_evento, id_lugar from sala_eventos.reservas where id_cliente = '{nif_cliente}'"
#    return run_query(comando)




def run_query(comando:str):
    try:
        connection = connect_bd()
        cursor = connection.cursor()

        cursor.execute(comando)
        
        dataset = cursor.fetchall()
        connection.close()

        return dataset
    except Error as e:
        return ("Error while connecting to MySQL", e)



def run_and_commit_query(comando:str):
    try:
        connection = connect_bd()
        cursor = connection.cursor()

        cursor.execute(comando)

        connection.commit()        
        connection.close()

        return True
    except Error as e:
        return ("Error while connecting to MySQL", e)

    