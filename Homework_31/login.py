import requests
from requests.auth import HTTPBasicAuth
import endpoints
import data


def test_login_user():
    for attempt in range(10):

        try:
            login_response = requests.post(endpoints.login_endopint, auth=HTTPBasicAuth(username='admin_user', password='12345678'))
            token = login_response.json().get('token')

            if token:
                print("Login successfull.")
                data.headers['Autorization'] = f'Bearer{token}'
                break

        except requests.RequestException as e:
            print(e)

    return data.headers

test_login_user()
