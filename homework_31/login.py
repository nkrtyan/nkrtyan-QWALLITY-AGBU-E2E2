import requests
import endpoints
import data
import logging


def test_login_user():
    login_body = {
        "username": data.register_body["username"],
        "password": data.register_body["password"]
    }

    for attempt in range(10):
        try:
            login_response = requests.post(endpoints.login_endpoint, json=login_body)
            token = login_response.json().get('token')

            if token:
                logging.info("Login successful.")
                print("Login successful.")
                data.headers['Authorization'] = f'Bearer {token}'
                break
            else:
                logging.error(f"Login failed: {login_response.status_code} {login_response.text}")

        except requests.RequestException as e:
            logging.warning(f"Attempt {attempt + 1}: login request failed - {e}")

    return data.headers