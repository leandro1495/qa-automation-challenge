import requests
import pytest
from .config.config import BASE_URL

@pytest.fixture(scope="module")
def session():
    """Crea una sesión para reutilizar conexiones."""
    with requests.Session() as s:
        yield s

@pytest.fixture
def new_user(session):
    """Crea un usuario antes de la prueba y lo elimina después."""
    user_data = {"name": "morpheus", "job": "leader"}
    response = session.post(f"{BASE_URL}/users", json=user_data)
    assert response.status_code == 201
    user = response.json()
    yield user
    session.delete(f"{BASE_URL}/users/{user['id']}")  # Cleanup

def test_get_users(session):
    """Prueba para obtener la lista de usuarios"""
    response = session.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data
    assert len(json_data["data"]) > 0  # Verificamos que haya usuarios

@pytest.mark.parametrize("name, job", [
    ("morpheus", "leader"),
    ("neo", "the one"),
])
def test_create_user(session, name, job):
    """Prueba para crear un usuario con diferentes datos"""
    user_data = {"name": name, "job": job}
    response = session.post(f"{BASE_URL}/users", json=user_data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["name"] == name
    assert response_data["job"] == job

def test_update_user(session, new_user):
    """Prueba para actualizar un usuario existente"""
    updated_data = {"name": "morpheus", "job": "zion resident"}
    response = session.put(f"{BASE_URL}/users/{new_user['id']}", json=updated_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["name"] == updated_data["name"]
    assert response_data["job"] == updated_data["job"]

def test_delete_user(session, new_user):
    """Prueba para eliminar un usuario"""
    response = session.delete(f"{BASE_URL}/users/{new_user['id']}")
    assert response.status_code == 204
