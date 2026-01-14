from tests.api_routers.test_post_routers import ensure_profile_exists

def user_with_profile(user_auth_client, test_user_2):
    res = user_auth_client.post("/profile/create", json={
        "password": test_user_2["password"],
        "date_of_birth": "2001-08-15",
        "hobby": "testing",
        "gender": "Male",
        "phone_number": "9875652146",
        "bio": "backend dev"
    })
    assert res.status_code == 200
    return test_user_2

def test_create_profile_success(auth_client,test_user):
    res = auth_client.post("/profile/create", json={
        "password": test_user["password"],
        "date_of_birth": "2001-08-15",
        "hobby": "testing",
        "gender": "Male",
        "phone_number": "9875652146",
        "bio": "this is not written by ai bro, tests are important write yourself!!"
    })
    assert res.status_code == 200

def test_create_profile_unauthorized(client):
    res = client.post("/profile/create", json={
        "bio": "Hacker mkc 3 baar!!"
    })
    assert res.status_code == 401

def test_view_own_profile(auth_client,test_user):
    ensure_profile_exists(auth_client, test_user["password"])
    res = auth_client.get("/profile/view")
    assert res.status_code == 200
    assert "bio" in res.json()

def test_view_profile_by_username(user_auth_client,client,test_user_2):
    user_with_profile(user_auth_client, test_user_2)
    res = client.get(f"/profile/view/{test_user_2["username"]}")
    assert res.status_code == 200
    assert "bio" in res.json()

def test_view_profile_by_username_not_exists(user_auth_client,client,test_user_2):
    res = client.get(f"/profile/view/{test_user_2["username"]}")
    assert res.status_code == 404
