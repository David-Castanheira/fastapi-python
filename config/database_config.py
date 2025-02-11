import mysql.connector
from dotenv import load_dotenv
import os 

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

def connection():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )
        
        print(f"Conexão com o banco estabelecida")
        return connection
    
    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco: {err}")
        return None
    
def open_cursor(connection):
    try:
        if connection:
            cursor = connection.cursor()
            return cursor
        else:
            print(f"Não foi possível estabelecer conexão com o banco para a criação do cursor")
            return None

    except mysql.connector.Error as err:
        print(f"Erro ao criar o cursor: {err}")
        return None
    
def close_cursor_connection(connection, cursor):
    try:
        if cursor:
            cursor.close()
            print(f"Conexão com o cursor interrompida")
        if connection:
            connection.close()
            print(f"Conexão com o banco interrompida")

    except mysql.connector.Error as err:
        print(f"Erro ao interromper a conexão ou o cursor: {err}")