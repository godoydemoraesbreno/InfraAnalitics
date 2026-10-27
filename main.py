from fastapi import FastAPI
from api.rotas import router

# variavel que guarda a aplicacao
app = FastAPI()

# rota raiz
@app.get("/")
async def root():
    return {'message': 'Hello world'}

# puxando o router pro app
app.include_router(router)