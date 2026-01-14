from pathlib import Path
import os

os.environ["ENV"] = "test"
os.environ["DATA_BASE"] = "postgresql+psycopg://postgres:wildwest@127.0.0.1:5433/fastapi_test"
os.environ["PEPPER_PASS"] = "test-pepper"

BASE_DIR = Path(__file__).resolve().parent

os.environ["ALGORITHM"] = "RS256"
os.environ["PRIVATE_KEY"] = (BASE_DIR / "test_private.pem").read_text()
os.environ["PUBLIC_KEY"] = (BASE_DIR / "test_public.pem").read_text()

import pytest
from sqlalchemy import text
from fastapi.testclient import TestClient
from app.main import app
from app.db.session import engine

@pytest.fixture(autouse=True)
def clean_tables():
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE likes, posts, profile, users RESTART IDENTITY CASCADE;"))
    yield

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture
def test_user(client):
    data = {
        "username": "testuser",
        "email_id": "test@example.com",
        "password": "StrongPass123"
    }
    res = client.post("/user/signup", json=data)
    assert res.status_code == 200
    return data

@pytest.fixture
def auth_client(client, test_user):
    res = client.post("/user/login", data={
        "username": test_user["email_id"],
        "password": test_user["password"]
    })
    assert res.status_code == 200

    token = res.json()["access_token"]
    client.headers.update({
        "Authorization": f"Bearer {token}"
    })
    return client

@pytest.fixture
def test_user_2(client):
    data = {
        "username": "testuser2",
        "email_id": "test2@example.com",
        "password": "StrongPass123"
    }
    res = client.post("/user/signup", json=data)
    assert res.status_code == 200
    return data

@pytest.fixture
def user_auth_client(client,test_user_2):
    res = client.post("/user/login", data={
        "username": test_user_2["email_id"],
        "password": test_user_2["password"]
    })
    assert res.status_code == 200

    token = res.json()["access_token"]
    client.headers.update({
        "Authorization": f"Bearer {token}"
    })
    return client