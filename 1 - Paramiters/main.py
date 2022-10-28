from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return {'Mensagem': 'Bem Vindo!!!'}

@app.get('/itens/{item_name}')
async def get_item(item_name: str):
    
    return {'Item_id': item_name}

