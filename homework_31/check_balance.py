import requests
import endpoints
import data


def get_current_balance():
    response = requests.get(endpoints.get_balance_endpoint, headers=data.headers)
    response.raise_for_status()
    return int(response.json().get("balance"))


def test_check_balance(balance_before):
    for attempt in range(10):
        try:
            check_balance_response = requests.get(endpoints.get_balance_endpoint, headers=data.headers)

            if check_balance_response.status_code == 200:
                response_data = check_balance_response.json()
                actual_balance = int(response_data.get("balance"))
                expected_balance = balance_before + data.add_balance_body["amount"]

                print("Balance retrieved successfully!")
                print("Current balance - ", actual_balance)

                assert actual_balance == expected_balance, (
                    f"Expected balance {expected_balance}, but got {actual_balance}"
                )
                print("Balance check passed!")
            else:
                print("Failed to get balance. Status code:", check_balance_response.status_code)
                print("Response:", check_balance_response.text)
            break

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Check balance failed. Retrying...")