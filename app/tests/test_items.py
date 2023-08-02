from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Item1", "price": 100.0, "description": "The very basic Item",})
    assert response.status_code == 200
    item = response.json()
    assert item["name"] == "Item1"
    assert item["price"] == 100.0
    assert "id" in item

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Item1", "price": 100.0, "description": "The very basic Item",}

def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 204
    assert response.content == b""

# This test should fail because we're trying to read a non-existing item
def test_read_non_existent_item():
    response = client.get("/items/999")
    assert response.status_code == 404
