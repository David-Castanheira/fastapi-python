import mysql.connector
from fastapi import FastAPI
from entities.users_entities import *
from config.database_config import connection

app = FastAPI()

conn = connection()

if conn:
    cursor = conn.cursor()
else:
    cursor = None

@app.get("/users", status_code=200)
async def list_users():
    if cursor:
        query_select = "SELECT * FROM User" 

        try:
            cursor.execute(query_select)
            users_result = cursor.fetchall()
            return users_result
        
        except mysql.connector.Error as err:
            print(f"Erro na conexão com o banco: {err}")
            return None
    else:
        return {"message": "Não foi possível obter conexão com o banco de dados para listar os usuários"}

# @app.post("/users", status_code=201)
# async def create_user():
#     if cursor:
#         query_insert = """
#         INSERT INTO User (first_name, last_name, gender, roles)
#         VALUES (%s, %s, %s, %s)
#         """
#         values = (User.first_name, User.last_name, User.gender, User.roles)

#         try:
#             cursor.execute(query_insert, values)
#             conn.commit()

#         except mysql.connector.Error as err:
#             print(f"Erro na conexão com o banco: {err}")
#             return None
#     else:
#         return {"message": "Não foi possível obter conexão com o banco de dados para criar o usuário"}

@app.get("/users/{user_id}", status_code=200)
async def get_user_by_id(user_id: int):
    if cursor:
        query_select_by_id = "SELECT * FROM User WHERE id=%s"
        cursor.execute(query_select_by_id, (user_id,))
        users_result_id = cursor.fetchone()
        return {"user_id": users_result_id}