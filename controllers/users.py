from fastapi import FastAPI
from entities.users_entities import *
from config.database_config import connection

app = FastAPI()

conn = connection()

if conn:
    cursor = conn.cursor()
else:
    cursor = None

@app.get("/users")
async def list_users():
    if cursor:
        query_select = "SELECT * FROM User" 
        cursor.execute(query_select)
        users_result = cursor.fetchall()
        return users_result
    else:
        return {"message": "Não foi possível obter conexão com o banco de dados para listar os usuários"}
    
@app.get("/users/{user_id}")
async def users_by_id(user_id):
    if cursor:
        query_select_by_id = "SELECT * FROM User WHERE id=%s"
        cursor.execute(query_select_by_id, user_id)
        users_result_id = cursor.fetchall
        return {"user_id": users_result_id}