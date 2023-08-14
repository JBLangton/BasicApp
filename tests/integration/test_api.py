# tests / integration / test_api.py
import logging
from fastapi.testclient import TestClient
import pytest
from app.main import app
from app.models.user import User

client = TestClient(app)

@pytest.fixture(scope="module")
def user_data():
    return {"name": "John", "email": "john@example.com"}

def test_create_user(user_data, clear_data):
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]
    assert "id" in data

# def test_read_user(user_data):
#     # Ideally, we'd get the user's ID from the fixture or another mechanism.
#     # For now, we'll hardcode an ID for the sake of the example.
#     user_id = 1
#     response = client.get(f"/users/{user_id}/")
#     assert response.status_code == 200
#     data = response.json()
#     assert data["name"] == user_data["name"]
#     assert data["email"] == user_data["email"]
#     assert data["id"] == user_id
