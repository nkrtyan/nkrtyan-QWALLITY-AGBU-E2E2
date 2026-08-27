import endpoints
import requests
import data
import logging


logger = logging.getLogger(__name__)


def test_Get_account_balance(headers):

    Get_account_balance_response = None

    logger.info("Starting Get Account Balance test")

    for attempt in range(10):

        try:
            logger.info(f"Attempt {attempt + 1}/10")

            Get_account_balance_response = requests.get(
                endpoints.Get_balance_endpoint,
                headers=headers
            )

            logger.info(
                f"Response status code: "
                f"{Get_account_balance_response.status_code}"
            )

            if Get_account_balance_response.status_code == 200:

                response_data = Get_account_balance_response.json()

                actual_balance = response_data.get("balance")

                logger.info(
                    f"Actual account balance: {actual_balance}"
                )

                logger.info("Successfully got the balance!")

                return actual_balance

            else:
                logger.warning(
                    f"Failed to get balance. "
                    f"Status code: "
                    f"{Get_account_balance_response.status_code}"
                )

        except requests.RequestException as e:

            logger.error(
                f"Request failed on attempt {attempt + 1}: {e}"
            )

    return actual_balance