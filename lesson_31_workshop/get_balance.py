import endpoints
import requests
import data
from logger_config import logger

def test_get_balance(headers):
    for attempt in range(10):

        try:
            get_balance_response = requests.get(endpoints.get_balance_endpoint, headers=headers)


            if get_balance_response.status_code == 200:
                response_data = get_balance_response.json()
                actual_balance = response_data.get("balance")

                logger.info("Successfully got the balance!")
                logger.info(f"Current balance - {actual_balance}")
                logger.info("Balance check passed!")

                # print("Successfully got the balance!")
                # print("Current balance - ", actual_balance)
                # print("Balance check passed!")
                break

        except requests.RequestException as e:
            logger.info({e})
            logger.error(f"Attempt {attempt + 1}: Check balance failed. Retrying...")

            # print(e)
            # print(f"Attempt {attempt + 1}: Check balance failed. Retrying...")