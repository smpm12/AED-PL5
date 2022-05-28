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
        #if connection.is_connected():
        #    db_Info = connection.get_server_info()
        #    print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("create table SALA (lugar varchar(3) not null, preco float not null, VIP boolean not null, PRIMARY KEY (lugar))")
        #record = cursor.fetchone()
        #print("You're connected to database: ", record)

        connection.close()
    except Error as e:
        print("Error while connecting to MySQL", e)
    