from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from uuid import uuid4
import json

app = FastAPI()

@app.get('/')
async def index():
    return {'Mensagem': 'Bem vindo!!!'}

@app.get('/listar/')
async def listar():
    return banco

@app.get('/listar/{id_animal}')
async def get_animal(id_animal: str):
    for ani in banco:
        if ani['id'] == id_animal:
            return ani
    raise HTTPException(status_code=404, detail='Animal not found')

class Animal(BaseModel):
    id: Optional[str]
    tipo: str
    raca: str
    cor: str
    nome: str
    sexo: str
    idade: int
    peso: float
    tamanho: float


with open('./Animais.json') as Animais:
    banco = json.load(Animais)

#banco = open('Animais.json', 'w')
#json.dump(banco)

@app.post('/cadastrar/')
async def cadastrar(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return animal

@app.delete('/delete/')
async def delete():
    id_animal: int
    deletado = banco.pop(id_animal)
    return {deletado:' Foi deletado com Sucesso!!'}
