from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from typing import List, Optional
import uvicorn


app = FastAPI()


class Item(BaseModel):
    id: Optional[str]
    produto: str
    quantidade: int
    valor: float
    total: float

class ItemResponse(BaseModel):
    produto: str
    quantidade: int

vendas: List[Item] = []

@app.get('/items')
async def get_itens():
    return vendas

@app.get('/items/{item_id}', response_model=ItemResponse)
async def get_item(item_id: str):
    for item in vendas:
        if item_id == item.id:
            return item
        raise HTTPException(status_code=404, detail='Item not found')

@app.post('/items')
async def create_item(item: Item):
    item.id = str(uuid4())
    vendas.append(item)
    return item

@app.put('/items/{item_id}')
async def update_item(item_id: str):
    return vendas

@app.delete('/items/{item_id}')
async def delete(item_id: str):
    for key, item in enumerate(vendas):
        if item_id == item.id:
            print(key)
            return vendas.pop(key)
    raise HTTPException(status_code=404, detail='Item not found')


if __name__ =='__main__':
    uvicorn.run(app)