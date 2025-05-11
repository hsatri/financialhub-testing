import requests

BASE_URL = "http://localhost:8000"

def test_add_budget_success(auth_header):
    payload = {
        "name": "My Monthly Budget",
        "amount": 10000
    }
    response = requests.post(f"{BASE_URL}/api/wallet/", headers=auth_header, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == payload["name"]

def test_add_budget_missing_fields(auth_header):
    payload = {
        "name": "",
        "amount": None
    }
    response = requests.post(f"{BASE_URL}/api/wallet/", headers=auth_header, json=payload)
    assert response.status_code == 400
