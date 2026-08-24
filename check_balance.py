import endpoints
import requests

def test_check_balance(headers):
    for attempt in range(10):
        try:
            response = requests.get(endpoints.get_balance_endpoint, headers=headers)
            
            if response.status_code == 200:
                print("Balance checked successfully!")
                balance_data = response.json()
                print(f"Current Balance Data: {balance_data}")
                break
            else:
                print("Failed to check balance. Status code:", response.status_code)
                print("Response:", response.text)
                
        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Check balance failed. Retrying...")