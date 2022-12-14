from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List, Optional
import uvicorn


app = FastAPI()


class Item():
    id: int 
    produto: str
    quantidade: int
    valor: int
    total: int

class ItemRequest(BaseModel):
    produto: Optional[str] = None
    quantidade: Optional[int] = None
    valor: Optional[int] = None

class ItemResponse(BaseModel):
    id: int
    produto: str
    total: int

vendas: List[Item] = []

@app.get('/items/')
async def get_itens():
    return vendas


@app.get('/items/{item_id}', response_model=ItemResponse)
async def get_item(item_id: int):
    for item in vendas:
        if item_id == item.id:
            prod ={
                "id": item.id,
                "produto": item.produto,
                "total": item.total 
            }
            print(prod)
            return prod
    raise HTTPException(status_code=404, detail='Item not found')
#commit

@app.post('/items/')
async def create_item(item_request: ItemRequest):
    item = Item()
    item.id = len(vendas) +1
    item.produto = item_request.produto
    item.quantidade = item_request.quantidade
    item.valor = item_request.valor
    item.total = item_request.quantidade * item_request.valor
    vendas.append(item)
    raise HTTPException(status_code=201, detail='Created')


@app.put('/items/{item_id}')
async def update_item(item_id: int, item_request: ItemRequest):
    item = Item()
    for key, item in enumerate(vendas):
        if item_id == item.id:
            vendas.pop(key)
            item.id = item_id
            item.produto = item_request.produto
            item.quantidade = item_request.quantidade
            item.valor = item_request.valor
            item.total = item_request.quantidade * item_request.valor
            vendas.insert(key, item)
            return item
    raise HTTPException(status_code=404, detail='Item not found')


@app.delete('/items/{item_id}')
async def delete(item_id: int,):
    for key, item in enumerate(vendas):
        if item_id == item.id:
            return vendas.pop(key)
            raise HTTPException(status_code=204, detail='resource deleted successfully') 

    raise HTTPException(status_code=404, detail='Item not found')


if __name__ =='__main__':
    uvicorn.run('main:app', reload=True)