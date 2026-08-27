import endpoints
import requests
import logging
from logging_conf import setup_logging


setup_logging()

def test_check_balance(headers):
    for attempt in range(10):
        try:
            get_added_balance_response = requests.get(endpoints.check_balance_endpoint, headers=headers)

            if get_added_balance_response.status_code == 200:
                amount = get_added_balance_response.json()
                current_balance = amount.get("balance")
                logging.info("Balance updated successfuly")
                logging.info("Current balance", current_balance)
                break

        except requests.RequestException as e:
            logging.error(f"Attempt {attempt + 1}: Check balance failed. Retrying...")
            logging.error(e)

    return current_balance