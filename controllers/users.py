import mysql.connector
from fastapi import APIRouter, HTTPException, status
from entities.users_entities import *
from config.database_config import connection, open_cursor, close_cursor_connection

router = APIRouter()

@router.get("/users", status_code=status.HTTP_302_FOUND)
def list_users():
    conn = None 
    cursor = None

    try:
        # Obtém a conexão
        conn = connection()
        if conn:
            # Obtém o cursor
            cursor = open_cursor(conn)
            if cursor:
                # Executa a query
                query_select = "SELECT * FROM User" 
                cursor.execute(query_select)
                users_result = cursor.fetchall()
                # Retorna os resultados
                return users_result  
            else:
                raise HTTPException(status_code=500, detail="Não foi possível criar o cursor.")
        else:
            raise HTTPException(status_code=500, detail="Não foi possível obter uma conexão com o banco.")
        
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuários: {err}")
    
    finally:
        # Encerra a conexão e o cursor
        close_cursor_connection(conn, cursor)

@router.get("/users/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int): 
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
                    return users_result_id
                else:
                    raise HTTPException(status_code=404, detail="Usuário não encontrado")
            else:
                raise HTTPException(status_code=500, detail="Não foi possível criar o cursor.")
        
        else:
            raise HTTPException(status_code=500, detail="Não foi possível obter uma conexão com o banco.")
        
    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco: {err}")
        conn.rollback()

    finally:
        close_cursor_connection(conn, cursor)

@router.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    conn = None
    cursor = None

    try:
        conn = connection()
        if conn:
            cursor = open_cursor(conn)

            if cursor:
                query_insert = """
                INSERT INTO User (first_name, last_name, gender, roles, email)
                VALUES (%s, %s, %s, %s, %s)
                """
                # Insere informações no banco e percorre a lista 'role' para atribuir um valor à ela
                values = (user.first_name, user.last_name, user.gender.value, ','.join([role.value for role in user.roles]), user.email)

                cursor.execute(query_insert, values)
                conn.commit()
                return {"message": "Usuário criado com sucesso!"}
            else:
                raise HTTPException(status_code=500, detail="Não foi possível criar o cursor.")
        else:
            raise HTTPException(status_code=500, detail="Não foi possível obter uma conexão com o banco.")

    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco: {err}")
        conn.rollback()

    finally:
        close_cursor_connection(conn, cursor)

@router.put("/users/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: User):
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
                roles = %s,
                email = %s,
                WHERE id = %s
                """

                # Atualiza as informações no banco e percorre a lista 'role' para atribuir um valor à ela
                values = (user.first_name, user.last_name, user.gender.value, ','.join([role.value for role in user.roles]), user.email, user_id)

                cursor.execute(query_update, values)
                conn.commit()
                return {"message": "Usuário atualizado com sucesso!"}
            else:
                raise HTTPException(status_code=500, detail="Não foi possível criar o cursor.")
        else:
            raise HTTPException(status_code=500, detail="Não foi possível obter uma conexão com o banco.")

    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco: {err}")
        conn.rollback()

    finally:
        close_cursor_connection(conn, cursor)

@router.delete("/users/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int):
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
                return {"message": "Usuário excluído com sucesso!"}
            else:
                raise HTTPException(status_code=500, detail="Não foi possível criar o cursor.")
        else:
            raise HTTPException(status_code=500, detail="Não foi possível obter uma conexão com o banco.")

    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco: {err}")
        conn.rollback()

    finally:
        close_cursor_connection(conn, cursor)