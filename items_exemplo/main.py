from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {'Mensagem': 'Bem Vindo!!!'}

@app.get('/itens/{item_id}')
async def get_item(item_id: int):
    return {'Item_id': item_id}

