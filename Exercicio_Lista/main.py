from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List, Optional
import uvicorn


app = FastAPI()


class Item(BaseModel):
    id: UUID 
    produto: str
    quantidade: int
    valor: float
    total: Optional[float]

class ItemUpdate(BaseModel):
    produto: Optional[str] = None
    quantidade: Optional[int] = None
    valor: Optional[float] = None

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
    item.id = uuid4()
    item.total = item.quantidade * item.valor
    vendas.append(item)
    raise HTTPException(status_code=201, detail='Created')

@app.put('/items/{item_id}')
async def update_item(item_id: UUID, itemup: Item):
    for key, item in enumerate(vendas):
        if item_id == item.id:
            vendas.pop(key)
            itemup.id = item_id
            itemup.total = itemup.quantidade * itemup.valor
            vendas.insert(key, itemup)
            return itemup
    raise HTTPException(status_code=404, detail='Item not found')

@app.delete('/items/{item_id}')
async def delete(item_id: str):
    for key, item in enumerate(vendas):
        if item_id == item.id:
            vendas.pop(key)
            raise HTTPException(status_code=204, detail='resource deleted successfully')

    raise HTTPException(status_code=404, detail='Item not found')


if __name__ =='__main__':
    uvicorn.run(app)