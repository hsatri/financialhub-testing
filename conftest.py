import pytest
import requests

BASE_URL = "http://localhost:8000"

@pytest.fixture
def test_user():
    return {"email": "testuser01@example.com", "password": "SecurePass123"}

@pytest.fixture
def auth_header(test_user):
    # Login and get JWT token
    login_response = requests.post(f"{BASE_URL}/api/token/", json=test_user)
    assert login_response.status_code == 200, "Login failed for fixture"
    token = login_response.json().get("access")
    return {"Authorization": f"Bearer {token}"}
