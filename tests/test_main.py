from app.main import app

def test_hello():
    client = app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data == {"message": "Hello, Docker!"}
