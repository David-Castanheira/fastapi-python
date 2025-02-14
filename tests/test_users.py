from fastapi.testclient import TestClient
from entities.users_entities import *
from controllers.users import *
from config.database_config import *
from app import * 
import httpx

client = TestClient(app)

def test_list_users():
    response = client.get("/users") 
    assert response.status_code == 302

def test_list_user_not_found():
    response = client.get("/users/1000") 
    assert response.status_code == 404
    assert response.json() == {"detail": "Usuário não encontrado"}

def test_create_user():
    response = client.post("/users", json={
    "first_name": "Teste3",
    "last_name": "teste",
    "gender": "male",
    "roles": ["user"],
    "email": "teste@teste3.com"
    }) 
    assert response.status_code == 201
    assert response.json() == {"message": "Usuário criado com sucesso!"}
    
def test_create_existing_user():
    response = client.post("/users", json={
	"first_name": "Teste",
	"last_name": "tests",
	"gender": "male",
	"roles": ["admin"],
	"email": "teste@test.com"
    }) 
    assert response.status_code == 409
    assert response.json() == {"detail": "Usuário já existente"}
