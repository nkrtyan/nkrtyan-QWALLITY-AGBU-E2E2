import requests
import endpoints
import data
import logging
from requests.auth import HTTPBasicAuth

def test_login_user(username, password):

    for attempt in range(10):

        try:
            login_reponse = requests.post(endpoints.login_endpoint, auth=HTTPBasicAuth(username=username, password=password))

            token = login_reponse.json().get('token')

            if token:
                logging.info("Login successful.")
                data.headers['Authorization'] = f'Bearer {token}'
                break

        except requests.RequestException as e:
            logging.info({e})
            logging.error(f"Attempt {attempt +1}: Login failed. Retrying...")

    return data.headers

if __name__ == "__main__":
    from register_user import test_register_user

    #Գրանցում ենք
    user, pwd = test_register_user()
    
    #Մուտք ենք գործում
    token = test_login_user(user, pwd)
    print("Received Token:", token)