import endpoints
import json
import requests
import data

old_balance = 100
added_balance = int(data.add_amount['amount'])
excepted_balance = old_balance + added_balance


def test_check_balance(headers):
    for attempt in range(10):
        try:
            get_added_balance_response = requests.get(endpoints.check_balance_endpoint, headers=headers)

            if get_added_balance_response:
                amount = get_added_balance_response.json()
                current_balance = int(amount["balance"])

                print("Old balance:", old_balance)
                print("Added balance:", added_balance)
                print("Expected balance:", excepted_balance)
                print("Current balance:", current_balance)

                if current_balance == excepted_balance:
                    print("Account Balance was updated correctly")

            else:
                print("Account Balance was not updated correctly")
                break


        except requests.RequestException as e:
            print(f"Attempt {attempt + 1}: Check balance failed. Retrying...")
            print(e)