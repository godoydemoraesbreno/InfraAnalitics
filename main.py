from fastapi import FastAPI
from api.rotas import router

app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'Hello world'}

app.include_router(router)