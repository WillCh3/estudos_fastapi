from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)

data = {
        "id": 1,
        "produto": "pacote figurinha", 
        "quantidade": 200,
        "valor": 3.0,
        "total": 600
        }


def test_create_item():
    response = client.post('/items/', json=data)
    assert response.status_code == 201
    assert response.json() == {"detail": "Created"}


def test_read_itens():
    response = client.get('/items/')
    assert response.status_code == 200
    assert data == response.json()[0]
    

def test_edit_item():
    response = client.put("/items/1", json={"produto": "teste", "quantidade": 0, "valor": 0})
    assert response.status_code == 200
    assert response.json() == {'id': 1, 'produto': 'teste', 'quantidade': 0, 'valor': 0, 'total': 0}

def test_delete_item():
    response = client.delete('/items/1', json=data)
    response.status_code == 200
    response.json() == {'id': 1, 'produto': 'teste', 'quantidade': 0, 'valor': 0, 'total': 0}
