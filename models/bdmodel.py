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
    try:
        connection = connect_bd()
        
        cursor = connection.cursor()
        cursor.execute("Select Nome, Data from `ual-pl05`.Eventos where data >= sysdate()")
        dataset = cursor.fetchall()
        
        connection.close()

        return dataset
    except Error as e:
        return ("Error while connecting to MySQL", e)



def get_sala():
    try:
        connection = connect_bd()
        
        cursor = connection.cursor()
        cursor.execute("SELECT id, Fila, Coluna, Lugar, Vip, Ativo, Preco FROM `ual-pl05`.Sala")
        dataset = cursor.fetchall()
        
        connection.close()

        return dataset
    except Error as e:
        return ("Error while connecting to MySQL", e)



def get_sala_n_filas():
    try:
        connection = connect_bd()
        
        cursor = connection.cursor()
        cursor.execute("SELECT max(Fila) FROM `ual-pl05`.Sala")
        dataset = cursor.fetchall()
        
        connection.close()

        return dataset[0][0]
    except Error as e:
        return ("Error while connecting to MySQL", e)



def get_sala_n_coluna():
    try:
        connection = connect_bd()
        
        cursor = connection.cursor()
        cursor.execute("SELECT max(Coluna) FROM `ual-pl05`.Sala")
        dataset = cursor.fetchall()
        
        connection.close()

        return dataset[0][0]
    except Error as e:
        return ("Error while connecting to MySQL", e)
        