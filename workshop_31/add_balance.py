import data
import requests
import endpoints

def test_add_balance(headers):
    balance_data = data.add_amount
    add_ammount = balance_data["amount"]

    for attempt in range (10):
        try:
            add_balance = requests.post(endpoints.add_balance_endpoint, json=balance_data, headers=headers)
            
            if add_balance.status_code == 200:
                print("Balance was added successfully")
                print(add_balance.json())
                break

            else:
                print("Adding balance failed. Status code: " ,add_balance.status_code)
                print("Response:", add_balance.text)

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt+1} failed. Retrying...")

    return add_ammount

