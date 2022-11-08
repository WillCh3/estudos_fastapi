from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from typing import List, Optional


app = FastAPI()


class Item(BaseModel):
    id: Optional[str]
    produto: str
    quantidade: int
    valor: float
    total: float

class ItemResponse(BaseModel):
    id: int
    produto: str
    quantidade: int
    valor: float
    total: float

vendas: List[Item] = []

@app.get('/items')
async def get_itens():
    return vendas

@app.get('/items/{item_id}')
async def get_item(item_id: str):
    for item in vendas:
        if item_id == item.id:
            return item

@app.post('/items')
def create_item(item: Item):
    item.id = str(uuid4())
    vendas.append(item)
    return item

@app.put('/items/{item_id}')
def update_item(item_id: int):
    
    return vendas
