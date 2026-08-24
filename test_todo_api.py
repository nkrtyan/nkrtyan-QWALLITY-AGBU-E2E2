import requests
from requests.auth import HTTPBasicAuth
import Endpoint
import data


register_response = requests.post(
    "https://qwallity-prod.onrender.com/register/api", 
    json=data.registor_body, 
    headers=data.headers
)
print("Register Status:", register_response.status_code)


def test_login_and_check_balance():
    try:
        
        login_response = requests.post(
            Endpoint.login_endpoint,
            json=data.login_body,
            headers=data.headers
        )

        print("Login Status:", login_response.status_code)
        print("Login Text:", login_response.text)

        
        if login_response.status_code == 200:
            token = login_response.json()["token"]

            auth_headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }

            
            balance_response = requests.post(
                Endpoint.balance_endpoint,  
                json=data.balance_body,
                headers=auth_headers
            )
            
            print("Add Balance Status:", balance_response.status_code)
            print("Add Balance Response:", balance_response.text)

            
            assert balance_response.status_code == 200, f"Expected 200, got {balance_response.status_code}"
            
            response_json = balance_response.json()
            print("Current Balance in System:", response_json)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")



test_login_and_check_balance()