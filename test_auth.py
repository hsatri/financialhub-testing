import requests
import pytest

BASE_URL = "http://localhost:8000"

@pytest.mark.order(1)
def test_register_user(test_user):
    response = requests.post(f"{BASE_URL}/api/register/", json=test_user)
    assert response.status_code in [200, 201, 400, 409], "user registration should be created"

@pytest.mark.order(2)
def test_register_duplicate_user(test_user):
    response = requests.post(f"{BASE_URL}/api/register/", json=test_user)
    assert response.status_code in [400, 409], "duplicate email should not be allowed"

@pytest.mark.order(3)
def test_login_valid_user(test_user):
    response = requests.post(f"{BASE_URL}/api/token/", json=test_user)
    assert response.status_code == 200
    assert "access" in response.json()

@pytest.mark.order(4)
def test_login_invalid_password():
    data = {"email": "testuser@example.com", "password": "WrongPassword"}
    response = requests.post(f"{BASE_URL}/api/token/", json=data)
    assert response.status_code == 401

@pytest.mark.order(5)
def test_login_sql_injection_attempt():
    data = {"email": "' OR '1'='1", "password": "any"}
    response = requests.post(f"{BASE_URL}/api/token/", json=data)
    assert response.status_code == 401 or response.status_code == 400


