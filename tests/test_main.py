import sys
import os
from app.main import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_hello():
    client = app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.data == b"Hello, Docker!"
