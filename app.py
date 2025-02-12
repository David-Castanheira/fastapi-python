import os
import uvicorn
from fastapi import FastAPI
from config.cors import *
from controllers.users import router as users_router

app = FastAPI()

# Inclui o router de users sem prefixo
app.include_router(users_router)

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de usuários!"}

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000)), reload=True)