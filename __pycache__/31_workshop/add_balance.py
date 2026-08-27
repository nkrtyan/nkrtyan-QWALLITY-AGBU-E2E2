import data
import requests
import endpoints
import logging
from logging_conf import setup_logging

setup_logging()

def test_add_balance(headers):
    balance_data = data.add_amount
    add_ammount = balance_data["amount"]

    for attempt in range (10):
        try:
            add_balance = requests.post(endpoints.add_balance_endpoint, json=balance_data, headers=headers)
            
            if add_balance.status_code == 200:
                logging.info("Balance was added successfully")
                logging.info(add_balance.json())
                break

            else:
                logging.error("Adding balance failed. Status code: " ,add_balance.status_code)
                logging.error("Response:", add_balance.text)

        except requests.RequestException as e:
            logging.error(e)
            logging.error(f"Attempt {attempt+1} failed. Retrying...")

    return add_ammount