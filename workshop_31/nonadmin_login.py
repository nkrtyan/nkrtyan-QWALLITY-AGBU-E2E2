import endpoints
import data
import requests
from requests.auth import HTTPBasicAuth
from register_user import test_register_user
import logging
from logging_conf import setup_logging

setup_logging()

username, password = test_register_user()

def test_login_user(username, password):
    for attempt in range(10):
        try: 
            login_response = requests.post(endpoints.login_endpoint, auth = HTTPBasicAuth(username=username, password=password))
            token = login_response.json().get("token")

            if token:
                logging.info("Login succesfull")
                data.headers["Authorization"] = f"Bareer {token}"
                break

        except requests.RequestException as e:
            print(e)
            print((f"Attempt {attempt + 1}: Login failed. Try again... "))

    return data.headers

if __name__ == "__main__":
    test_login_user(username, password)         