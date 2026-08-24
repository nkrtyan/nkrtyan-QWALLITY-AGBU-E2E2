import requests
import endpoints
import data
from logger_config import logger


def test_add_balance(headers):
    balance_data = data.balance_body

    for attempt in range(10):

        try:
            add_balance_response = requests.post(endpoints.add_balance_endpoint, json=balance_data, headers=headers)


            if add_balance_response.status_code == 200:
                logger.info("Balance added successfully.")
                logger.info(f"{add_balance_response.json()}")

                # print("Balance added successfully.")
                # print(add_balance_response.json())
                break

            else:
                logger.error(f'Failed to add balance. Status code: {add_balance_response.status_code}')
                logger.info(f"Response: {add_balance_response.text}")

                # print("Failed to add balance. Status code:", add_balance_response.status_code)
                # print("Response:", add_balance_response.text)
                


        except requests.RequestException as e:
            logger.info({e})
            logger.error(f"Attempt {attempt + 1}: Add balance failed. Retrying...")

            # print(e)
            # print(f"Attempt {attempt + 1}: Add balance failed. Retrying...")

    return add_balance_response

