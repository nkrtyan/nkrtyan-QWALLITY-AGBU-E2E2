import endpoints
import data
import requests
import logging

def test_register_user():
    register_data = data.register_body
    username = register_data["username"]
    password = register_data["password"]
    default_amount = register_data["account"]

    for attempt in range(10):
        try:
            register_user_response = requests.post(endpoints.register_endpoint, json=register_data, headers=data.headers)

            if register_user_response:
                logging.info("User registered successfully!")
                logging.info(f"Username - {username}")
                logging.info(f"Password - {password}")                
                break

        except requests.exceptions.RequestException as e:
            logging.info({e})
            logging.error(f"Attempt {attempt + 1}: Register failed with error: {e}")

    return username, password, int(default_amount)


if __name__ == "__main__":
    test_register_user()