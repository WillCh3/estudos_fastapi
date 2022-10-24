from typing import Union
from fastapi import FastAPI

app = FastAPI()

vendas = {1:{'Produto':'Televisor 55', 'Quantidade': 5, 'Valor':3.500, 'Total':17.500},
          2:{'Produto':'Batedeira', 'Quantidade': 10, 'Valor':350, 'Total':3500},
          3:{'Produto':'celular', 'Quantidade': 17, 'Valor':1.500, 'Total':25.500},
          4:{'Produto':'liquidificador', 'Quantidade': 3, 'Valor':280, 'Total':840},
          5:{'Produto':'notebook', 'Quantidade': 7, 'Valor':3.500, 'Total':24.500},}

@app.get('/')
async def index():
    return {'Mensagem': 'Bem vindo!!!'}

@app.get('/vendas/{item_id}')
async def pegar_venda(item_id: int):
    if item_id in vendas:
        return vendas[item_id]
    else:
        return {'Mensagem': 'Esse numero de venda não consta nos índices'}