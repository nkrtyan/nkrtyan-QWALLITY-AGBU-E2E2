import requests
import Endpoint
import data

def test_login_user():
    try:
        login_response = requests.post(
            Endpoint.login_endpoint,
            json=data.login_body,
            headers=data.headers
        )

        print("Login Status:", login_response.status_code)

        if login_response.status_code == 200:
            token = login_response.json()["token"]

            auth_header = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
            return auth_header
        else:
            print("Login failed:", login_response.text)
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None