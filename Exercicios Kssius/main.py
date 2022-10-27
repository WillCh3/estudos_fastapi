from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

vendas = {1:{'Produto':'Televisor 55', 'Quantidade': 5, 'Valor':3.500, 'Total':17.500},
          2:{'Produto':'Batedeira', 'Quantidade': 10, 'Valor':350, 'Total':3500},
          3:{'Produto':'celular', 'Quantidade': 17, 'Valor':1.500, 'Total':25.500},
          4:{'Produto':'liquidificador', 'Quantidade': 3, 'Valor':280, 'Total':840},
          5:{'Produto':'notebook', 'Quantidade': 7, 'Valor':3.500, 'Total':24.500},
        }


app = FastAPI()



class Item(BaseModel):
    Produto: str
    Quantidade: int
    Valor: float
    Total: float

class User_out(BaseModel):
    Produto: str
    Valor: float
    Total: float


@app.get('/')
async def index():
    return {'Mensagem':'Seja bem vindo!'}

@app.get('/vendas/{item_id}', response_model=Item, response_model_exclude={'Quantidade'})
async def get_vendas(item_id: int):
    if item_id in vendas:
        return vendas[item_id]
    else:
        raise HTTPException(status_code=404, detail='Item not found')


@app.post('/items')
async def create_item(item: Item):
    vendas[len(vendas) + 1] = {
        'Produto': item.Produto,
        'Quantidade': item.Quantidade,
        'Valo': item.Valor,
        'Total': item.Quantidade * item.Valor
    }
    return item


@app.get('/items')
async def list_items():
    return vendas


@app.get('/pesquisa/')
async def read_items(init: int = 1, limit: int = 3 ):
    resp ={}
    for item in range(init, limit + 1):
        resp[item] = vendas[item]
    return resp


@app.get('/pesquisa/{id_item}')
async def get_item(id_item: int):
    if id_item in vendas:
        res = vendas.get(id_item)
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    return res

@app.delete('/delete/{id_item}')
async def delete(id_item: int):
    if id_item in vendas:
        return vendas.pop(id_item)
    else:
        raise HTTPException(status_code=404, detail="Item not found")