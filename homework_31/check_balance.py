import requests
import endpoints
import data
import logging


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
                logging.info(f"Balance check passed: {actual_balance}")
                print("Balance check passed!")
            else:
                logging.error(f"Check balance failed: {check_balance_response.status_code} {check_balance_response.text}")
                print("Failed to get balance. Status code:", check_balance_response.status_code)
            break

        except requests.RequestException as e:
            logging.warning(f"Attempt {attempt + 1}: check balance request failed - {e}")
            print(e)