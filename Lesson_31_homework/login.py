import requests
import endpoints
import data


def test_login_user(username, password):
    login_data = {
        "username": username,
        "password": password
    }

    login_response = requests.post(endpoints.login_endpoint, json=login_data, headers=data.headers)

    if login_response.status_code == 200:
        print("\nLogin successful!")
        token = login_response.json().get("access_token")
        return token
    else:
        print("\nLogin failed. Status code:", login_response.status_code)
        print("Response:", login_response.text)
        return None