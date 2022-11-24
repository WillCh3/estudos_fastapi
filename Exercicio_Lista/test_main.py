from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)

data = {}

dados = {
            "produto": "4",
            "quantidade": 10,
            "valor": 5
        }

edit = {
            "produto": "teste",
            "quantidade": 0,
            "valor": 0
        }



def test_read_itens():
    response = client.get('/items')
    assert response.status_code == 200
    assert response.json() == []

def test_read_item():
    response_post = client.post('/items', json=dados)
    print(response_post.json())
    response = client.get('/items/'+response_post.json()['id'])
    assert response.status_code == 200
    assert response.json()['produto'] == '4'
    assert response.json()['total'] == 50



def test_create_item():
    response = client.post('/items', json=dados)
    assert response.status_code == 200
    assert response.json()['produto'] == "4"
    

def test_edit_item():
    response_post = client.post('/items', json=dados)
    print(response_post.json())
    response = client.put("/items/" + response_post.json()['id'], json=edit )
    assert response.status_code == 200
    assert response.json() == {
                                "id": response_post.json()['id'],
                                "produto": "teste",
                                "quantidade": 0,
                                "valor": 0,
                                "total": 0
                                }

def test_delete_item():
    response_post = client.post('/items', json=dados)
    response = client.delete('/items/'+ response_post.json()['id'])
    assert response.status_code == 204
    

#commit