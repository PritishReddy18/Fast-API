def test_signup_success(client):
    res = client.post("/user/signup", json={
        "username": "devuser",
        "email_id": "dev@example.com",
        "password": "StrongPass123"
    })
    assert res.status_code == 200

def test_signup_duplicate_user(client):
    client.post("/user/signup", json={
        "email_id": "dupuser@google.com",
        "username": "dupuser",
        "password": "StrongPass123"
    })

    res = client.post("/user/signup", json={
        "email_id": "dupuser2@example.com",
        "username": "dupuser",
        "password": "StrongPass123"
    })
    assert res.status_code in (400, 409)


def test_signup_missing_fields(client):
    res = client.post("/user/signup", json={
        "username": "nouser"
    })
    assert res.status_code == 422


def test_login_success(test_user, client):
    res = client.post("/user/login", data={
        "username": test_user["email_id"],  # email here
        "password": test_user["password"]
    })
    assert res.status_code == 200

def test_login_wrong_password(test_user, client):
    res = client.post("/user/login", data={
        "username": test_user["email_id"],
        "password": "wrongpass"
    })
    assert res.status_code == 401
