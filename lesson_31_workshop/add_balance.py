import requests
import endpoints
import data
import logging

def test_add_balance(headers):
    balance_data = data.balance_body
    add_amount = balance_data["amount"]

    for attempt in range(10):

        try:
            add_balance_response = requests.post(endpoints.add_balance_endpoint, json=balance_data, headers=headers)

            if add_balance_response.status_code == 200:
                logging.info("Balance added successfully.")
                logging.info(f"{add_balance_response.json()}")
                break

            else:
                logging.error(f'Failed to add balance. Status code: {add_balance_response.status_code}')
                logging.info(f"Response: {add_balance_response.text}")

        except requests.RequestException as e:
            logging.info({e})
            logging.error(f"Attempt {attempt + 1}: Add balance failed. Retrying...")

    return int(add_amount)

