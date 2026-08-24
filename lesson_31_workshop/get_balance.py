import endpoints
import requests
import data

def test_get_balance(headers):
    for attempt in range(10):

        try:
            get_balance_response = requests.get(endpoints.get_balance_endpoint, headers=data.headers)


            if get_balance_response.status_code == 200:
                response_data = get_balance_response.json()
                actual_balance = response_data.get("balance")
                print("Balance retrieved successfully!")
                print("Current balance - ", actual_balance)
                print("Balance check passed!")
                break

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Check balance failed. Retrying...")