import mysql.connector
from fastapi import FastAPI, HTTPException, status
from entities.users_entities import *
from config.database_config import connection, open_cursor, close_cursor_connection

app = FastAPI()

@app.get("/users", status_code=status.HTTP_302_FOUND)
async def list_users():
    conn = None 
    cursor = None

    try:
        # 1. Obtém a conexão
        conn = connection()
        if conn:
            # 2. Obtém o cursor
            cursor = open_cursor(conn)
            if cursor:
                # 3. Executa a query
                query_select = "SELECT * FROM User" 
                cursor.execute(query_select)
                users_result = cursor.fetchall()
                # 4. Retorna os resultados
                return users_result  
            else:
                raise HTTPException(status_code=500, detail="Não foi possível a criação cursor.")
        else:
            raise HTTPException(status_code=500, detail="Não foi possível obter uma conexão com o banco.")
        
    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco: {err}")
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuários: {err}")
    
    finally:
        # 5. Encerra a conexão e o cursor
        close_cursor_connection(conn, cursor)

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: int): 
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn:
            cursor = open_cursor(conn)

            if cursor:
                query_select_by_id = "SELECT * FROM User WHERE id=%s"
                cursor.execute(query_select_by_id, (user_id,))
                users_result_id = cursor.fetchone()
                if users_result_id:
                    return {"records": users_result_id}
                else:
                    raise HTTPException(status_code=404, detail="Usuário não encontrado")
            else:
                raise HTTPException(status_code=500, detail="Não foi possível a criação cursor.")
        
        else:
            raise HTTPException(status_code=500, detail="Não foi possível obter uma conexão com o banco.")
        
    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco: {err}")
        conn.rollback()

    finally:
        close_cursor_connection(conn, cursor)

@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn:
            cursor = open_cursor(conn)

            if cursor:
                query_insert = """
                INSERT INTO User (first_name, last_name, gender, roles)
                VALUES (%s, %s, %s, %s)
                """
                values = (user.first_name, user.last_name, user.gender.value, ','.join([role.value for role in user.roles]))

                cursor.execute(query_insert, values)
                conn.commit()
            else:
                raise HTTPException(status_code=500, detail="Não foi possível a criação cursor.")
        else:
            raise HTTPException(status_code=500, detail="Não foi possível obter uma conexão com o banco.")

    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco: {err}")
        conn.rollback()

    finally:
        close_cursor_connection(conn, cursor)

@app.put("/users/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: User):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn:
            cursor = open_cursor(conn)

            if cursor:
                query_update = """
                UPDATE User SET first_name = %s, 
                last_name = %s,
                gender = %s,
                roles = %s
                WHERE id = %s
                """

                values = (user.first_name, user.last_name, user.gender.value, ','.join([role.value for role in user.roles]), user_id)

                cursor.execute(query_update, values)
                conn.commit()
            else:
                raise HTTPException(status_code=500, detail="Não foi possível a criação cursor.")
        else:
            raise HTTPException(status_code=500, detail="Não foi possível obter uma conexão com o banco.")

    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco: {err}")
        conn.rollback()

    finally:
        close_cursor_connection(conn, cursor)

@app.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
async def delete_users(user_id: int):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn:
            cursor = open_cursor(conn)

            if cursor:
                query_delete = "DELETE FROM User WHERE id = %s"
                cursor.execute(query_delete, (user_id,))
                conn.commit()
            else:
                raise HTTPException(status_code=500, detail="Não foi possível a criação cursor.")
        else:
            raise HTTPException(status_code=500, detail="Não foi possível obter uma conexão com o banco.")

    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco: {err}")
        conn.rollback()

    finally:
        close_cursor_connection(conn, cursor)