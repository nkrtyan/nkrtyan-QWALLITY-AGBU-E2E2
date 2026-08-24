import endpoints
import data
import requests
from logger_config import logger

def test_register_user():
    register_data = data.register_body
    username = register_data["username"]
    password = register_data["password"]

    for attempt in range(10):
        try:
            register_user_response = requests.post(endpoints.register_endpoint, json=register_data, headers=data.headers)

            if register_user_response:
                # print("User registered succesfully!")
                # print(register_user_response.json())
                # print("Username - ", username)
                # print("Password - ", password)
                
                logger.info("User registered successfully!")
                logger.info(f"Username - {username}")
                logger.info(f"Password - {password}")                
                break

        except requests.exceptions.RequestException as e:
            logger.info({e})
            logger.error(f"Attempt {attempt + 1}: Register failed with error: {e}")

            # print(e)
            # print(f"Attempt {attempt + 1}: Register failed. Retrying...")

    return username, password

if __name__ == "__main__":
    test_register_user()