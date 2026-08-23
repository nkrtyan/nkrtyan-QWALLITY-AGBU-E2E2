import requests
import data
import endpoints


def test_register_user():
    response = requests.post(
        endpoints.register_endpoint,
        json=data.register_body
    )

    assert response.status_code == 201

    print("User registered successfully.")
    print("Username:", data.register_body["username"])
    print("Password:", data.register_body["password"])