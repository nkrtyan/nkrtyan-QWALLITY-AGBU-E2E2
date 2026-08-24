import requests
import endpoints
import data
from logger_config import logger

def test_login_user(username, password):
    login_body = {
        "username": username,
        "password": password
    }
    

    for attempt in range(10):

        try:
            login_reponse = requests.post(endpoints.login_endpoint, json=login_body)
            token = login_reponse.json().get('token')

            if token:
                # print("Login successful.")
                logger.info("Login successful.")
                data.headers['Authorization'] = f'Bearer {token}'
                break

        except requests.RequestException as e:
            logger.info({e})
            logger.error(f"Attempt {attempt +1}: Login failed. Retrying...")

            # print(e)
            # print(f"Attempt {attempt +1}: Login failed. Retrying...")

    return data.headers

if __name__ == "__main__":
    from register_user import test_register_user

    #Գրանցում ենք
    user, pwd = test_register_user()
    
    #Մուտք ենք գործում
    token = test_login_user(user, pwd)
    print("Received Token:", token)