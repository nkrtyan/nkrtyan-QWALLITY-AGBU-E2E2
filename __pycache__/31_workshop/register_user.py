import data
import endpoints
import requests
import logging
from logging_conf import setup_logging


setup_logging()

def test_register_user():
    register_data = data.register_body
    username = register_data["username"]
    password = register_data["password"]
    account = register_data["account"]


    for attempt in range(10):
        try:
            register_user_response = requests.post(endpoints.register_endpoint, json=register_data, headers=data.headers)

            if register_user_response.status_code == 201:
                logging.info("User registered successfully. Username: %s | Password: %s | Account: %s",
                             username,
                             password,
                             account)
                logging.info(register_user_response.json())
                break
            else:
                logging.error("Registration is failed. Status code: %s", register_user_response.status_code)
                logging.error("Registration response: %s", register_user_response.text)

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Register failed. Retrying...")

    
    return username, password, account


if __name__ == "__main__":
    test_register_user()