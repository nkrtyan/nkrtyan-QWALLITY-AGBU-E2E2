import requests
import Endpoint
import data

def test_check_balance(headers):
  
    check_response = requests.post(
        Endpoint.balance_endpoint,
        json=data.balance_body,
        headers=headers
    )
    
    print("4. Check Balance Status:", check_response.status_code)
    print("Balance Data:", check_response.text)
    
    assert check_response.status_code == 200, f"Expected 200, got {check_response.status_code}"