import endpoints
import data
import requests

def test_add_balance(headers):
    for attempt in range(10):
        try:
            response = requests.post(
                endpoints.add_balance_endpoint, 
                json=data.add_balance_body, 
                headers=headers
            )
            
            if response.status_code == 200 or response.status_code == 201:
                print("Account balance added successfully!")
                print(response.json())
                break
            else:
                print("Failed to add balance. Status code:", response.status_code)
                print("Response:", response.text)
                
        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Add balance failed. Retrying...")

        