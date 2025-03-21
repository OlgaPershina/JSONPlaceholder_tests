
import requests
pytest

BASE_URL = "https://jsonplaceholder.typicode.com/"  


def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code != 404, "Status code is 404"
    assert response.status_code == 200, "Status code is not 200"


def test_create_new_post():
    data = {
        "userId": 1,
        "title": "My testing new post",
        "body": "Something very interesting for my team"
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    assert response.status_code in [200, 201], "POST request failed"
    response_json = response.json()
    assert response_json is not None, "Response JSON is undefined"
    return response_json['id']


def test_get_new_post():
    post_id = test_create_new_post()
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200, "GET request for new post failed"


def test_update_post():
    post_id = test_create_new_post()
    updated_data = {
        "userId": 1,
        "title": "Updated post title",
        "body": "Updated post content"
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_data)
    assert response.status_code in [200, 201, 204], "PUT request failed"
