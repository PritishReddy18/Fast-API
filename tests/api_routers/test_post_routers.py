def ensure_profile_exists(auth_client, password):
    res = auth_client.get("/profile/view")
    if res.status_code == 404:
        create_res = auth_client.post("/profile/create", json={
            "password": password,
            "date_of_birth": "2001-08-15",
            "hobby": "testing",
            "gender": "Male",
            "phone_number": "9875652146",
            "bio": "testing for fun, not for joy"
        })
        assert create_res.status_code == 200

def test_create_post_success(auth_client, test_user):
    ensure_profile_exists(auth_client, test_user["password"])
    res = auth_client.post("/posts/create", json={
        "title": "My First Post",
        "content": "Hello world"
    })
    assert res.status_code == 200
    assert res.json()["title"] == "My First Post"

def test_create_post_unauthorized(client):
    res = client.post("/posts/create", json={
        "title": "this is called the title",
        "content": "called title, why?? it called title?? i dont even know why?? bruh.."
    })
    assert res.status_code == 401

def ensure_posts_exists(auth_client,test_user):
    res = auth_client.get("/posts/view")
    if res.status_code == 404:
        test_create_post_success(auth_client, test_user)

def test_get_user_posts(auth_client,test_user):
    ensure_posts_exists(auth_client, test_user)
    res = auth_client.get("/posts/view")
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data,list)
    assert len(data) > 0

def test_get_user_posts_unauthorized(client):
    res = client.get("/posts/view")
    assert res.status_code == 401
