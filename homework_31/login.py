import requests
import data
import endpoints


def test_login_user():
    login_body = {
        "username": data.register_body["username"],
        "password": data.register_body["password"]
    }

    response = requests.post(
        endpoints.login_endpoint,
        json=login_body
    )

    assert response.status_code == 200

    token = response.json()["token"]
    data.headers["Authorization"] = f"Bearer {token}"

    print("Login successful.")