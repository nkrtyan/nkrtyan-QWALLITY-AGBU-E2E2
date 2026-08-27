import requests
import endpoints
import data
import logging


logger = logging.getLogger(__name__)


def test_add_account_balance(headers):
    balance_data = data.balance_body

    logger.info("Starting Add Account Balance test")
    logger.info(f"Balance data: {balance_data}")

    for attempt in range(10):
        try:
            logger.info(f"Attempt {attempt + 1}/10")

            Add_account_balance_response = requests.post(
                endpoints.Add_balance_endpoint,
                json=balance_data,
                headers=headers
            )

            logger.info(
                f"Response status code: "
                f"{Add_account_balance_response.status_code}"
            )

            if Add_account_balance_response.status_code == 200:
                logger.info("Balance added successfully.")
                break

            else:
                logger.warning(
                    f"Balance was not added. "
                    f"Response: {Add_account_balance_response.text}"
                )

        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")

    return Add_account_balance_response