import data
import endpoints
import requests
import logging


def test_register_user():
    register_data = data.register_body
    username = register_data["username"]
    password = register_data["password"]

    for attempt in range(10):
        try:
            response = requests.post(endpoints.register_endpoint, json=register_data)
            logging.debug(f"Register response: {response.status_code} {response.text}")

            if response.status_code == 201:
                logging.info(f"User registered successfully: {username}")
                print("User registered successfully.")
                print("Username:", username)
                print("Password:", password)
            else:
                logging.error(f"Register failed: {response.status_code} {response.text}")
                print("Failed to register user. Status code:", response.status_code)
            break

        except requests.RequestException as e:
            logging.warning(f"Attempt {attempt + 1}: register request failed - {e}")

    return username, password

