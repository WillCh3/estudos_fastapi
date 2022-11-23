from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

data = {}

dados = { "produto": "pacote figurinha", "quantidade": 200, "valor": 3.0}

def test_read_itens():
    response = client.get('/items')
    assert response.status_code == 200
    assert response.json() == []


def test_create_item():
    response = client.post('/items', json=dados)
    assert response.status_code == 201
    assert response.json() == {"detail": "Created"}
    

def test_edit_item():
    response = client.put("/items/{data['id']}", json=dados )
    assert response.status_code == 200
    data = response.json()
    assert data['produto'] == 'pacote figurinha'

def test_delete_item():
    response = client.delete('/items/')
    response.status_code == 200

#commit