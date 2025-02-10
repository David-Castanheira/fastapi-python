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
