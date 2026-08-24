import requests
import Endpoint
import data

def test_add_balance(headers):
    
    add_balance_response = requests.post(
        Endpoint.balance_endpoint,
        json=data.balance_body,
        headers=headers
    )
    
    print("3. Add Balance Status:", add_balance_response.status_code)
    print("Add Balance Response:", add_balance_response.text)
    
    assert add_balance_response.status_code == 200, f"Expected 200, got {add_balance_response.status_code}"