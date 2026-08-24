import data
import requests
import endpoints

def test_add_balance(headers):
    for attempt in range (10):
        try:
            add_balance = requests.post(endpoints.add_balance_endpoint, json=data.add_amount, headers=data.headers)
            balance = add_balance.json().get("amount")

            if balance:
                print(f"{balance} was added successfully")
                break

            else:
                print("Adding balance failed. Status code: " ,add_balance.status_code)

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt+1} failed. Retrying...")

    return balance

