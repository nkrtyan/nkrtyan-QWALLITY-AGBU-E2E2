import endpoints
import data
import requests
from requests.auth import HTTPBasicAuth

def test_login_admin():
    for attempt in range(10):
        try: 
            login_response = requests.post(endpoints.login_endpoint, auth = HTTPBasicAuth(username="admin_user", password="11111111"))
            token = login_response.json().get("token")

            if token:
                print("Login succesfull")
                data.headers["Authorization"] = f"Bareer {token}"
                break

        except requests.RequestException is e:
            print(e)
            print((f"Attempt {attempt + 1}: Login failed. Try again... "))

    return data.headers

test_login_admin()
            

