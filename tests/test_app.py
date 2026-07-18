def test_index_page_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Chloe Kwon" in response.data


def test_hobbies_page_loads(client):
    response = client.get("/hobbies")

    assert response.status_code == 200
    assert b"Hiking" in response.data


def test_timeline_page_loads(client):
    response = client.get("/timeline")

    assert response.status_code == 200


def test_status_page_loads(client):
    response = client.get("/status")

    assert response.status_code == 200
    assert b"Server Status" in response.data


def test_system_status_returns_resource_usage(client):
    response = client.get("/api/system_status")

    assert response.status_code == 200
    body = response.get_json()
    assert body["db"] in ("ok", "error")
    assert 0 <= body["cpu"]["percent"] <= 100
    assert 0 <= body["memory"]["percent"] <= 100
    assert 0 <= body["disk"]["percent"] <= 100
    assert body["memory"]["total_gb"] > 0
    assert body["disk"]["total_gb"] > 0


def test_post_timeline_post_creates_entry(client):
    response = client.post(
        "/api/timeline_post",
        data={"name": "Ada Lovelace", "email": "ada@example.com", "content": "Excited to join the fellowship!"},
    )

    assert response.status_code == 200
    body = response.get_json()
    assert body["name"] == "Ada Lovelace"
    assert body["content"] == "Excited to join the fellowship!"


def test_get_timeline_posts_returns_created_posts(client):
    client.post(
        "/api/timeline_post",
        data={"name": "Ada Lovelace", "email": "ada@example.com", "content": "First post"},
    )

    response = client.get("/api/timeline_post")

    assert response.status_code == 200
    posts = response.get_json()["timeline_posts"]
    assert len(posts) == 1
    assert posts[0]["content"] == "First post"


def test_get_timeline_posts_empty_when_none_created(client):
    response = client.get("/api/timeline_post")

    assert response.status_code == 200
    assert response.get_json()["timeline_posts"] == []


def test_post_timeline_post_missing_field_returns_400(client):
    response = client.post(
        "/api/timeline_post",
        data={"name": "Ada Lovelace", "email": "ada@example.com"},
    )

    assert response.status_code == 400
