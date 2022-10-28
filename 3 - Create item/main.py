from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

vendas = {1:{'Produto':'Televisor 55', 'Quantidade': 5, 'Valor':3.500, 'Total':17.500},
          2:{'Produto':'Batedeira', 'Quantidade': 10, 'Valor':350, 'Total':3500},
          3:{'Produto':'celular', 'Quantidade': 17, 'Valor':1.500, 'Total':25.500},
          4:{'Produto':'liquidificador', 'Quantidade': 3, 'Valor':280, 'Total':840},
          5:{'Produto':'notebook', 'Quantidade': 7, 'Valor':3.500, 'Total':24.500},}


app = FastAPI()

@app.get('/')
async def index():
    return {'Mensagem': 'Bem vindo!!'}

@app.get('/vendas/{item_id}')
async def get_vendas(item_id: int):
    if item_id in vendas:
        return vendas[item_id]
    else:
        raise HTTPException(status_code=404, detail='Item not found.')


class Item(BaseModel):
    Produto: str
    Quantidade: int
    Valor: float
    Total: float


@app.post("/items/")
async def create_item(item: Item):
    vendas[len(vendas) + 1] = {
            'Produto': item.Produto,
            'Quantidade': item.Quantidade,
            'Valor': item.Valor,
            'Total': item.Quantidade * item.Valor
    }
    return item

