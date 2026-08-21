import requests
from requests.auth import HTTPBasicAuth
import endpoints
import data

def test_login_user():
    for attempt in range(10):

        try:
            login_reponse = requests.post(endpoints.login_endpoint, auth=HTTPBasicAuth(username="non_admin_user", password="11111111"))
            token = login_reponse.json().get('token')

            if token:
                print("Login successful.")
                data.headers['Authorization'] = f'Bearer {token}'
                break

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt +1}: Login failed. Retrying...")

    return data.headers

test_login_user()
    