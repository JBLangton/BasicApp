# tests / unit / test_user.py
import logging
import pytest
from app.models.user import User

@pytest.fixture(scope="module")
def user_data():
    return {"name": "John", "email": "john@example.com"}

def test_create_user(user_data):
    user = User(name=user_data["name"], email=user_data["email"])
    assert user.name == user_data["name"]
    assert user.email == user_data["email"]
