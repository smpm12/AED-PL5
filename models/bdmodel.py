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