from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test valid login
def test_login():
    response = client.post(
        "/token",
        data={"username": "admin", "password": "userpass"},
    )
    assert response.status_code == 200
    json_response = response.json()
    assert "Authenticated_user" in json_response
    assert json_response["Authenticated_user"] == "admin"

# Test invalid login
def test_login_invalid_credentials():
    response = client.post(
        "/token",
        data={"username": "wronguser", "password": "wrongpass"},
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Incorrect username or password"
    }
