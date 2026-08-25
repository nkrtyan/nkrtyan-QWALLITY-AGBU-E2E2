import endpoints
import requests
import logging

def test_get_balance(headers):
    for attempt in range(10):

        try:
            get_balance_response = requests.get(endpoints.get_balance_endpoint, headers=headers)

            if get_balance_response.status_code == 200:
                response_data = get_balance_response.json()
                actual_balance = response_data.get("balance")

                logging.info("Successfully got the balance!")
                logging.info(f"Current balance - {actual_balance}")
                logging.info("Balance check passed!")
                break

        except requests.RequestException as e:
            logging.info({e})
            logging.error(f"Attempt {attempt + 1}: Check balance failed. Retrying...")

    return float(actual_balance)