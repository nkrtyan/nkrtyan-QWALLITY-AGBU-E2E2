import requests
import endpoints
import data
import logging


def test_add_balance():
    balance_data = data.add_balance_body

    for attempt in range(10):
        try:
            add_balance_response = requests.post(
                endpoints.add_balance_endpoint,
                json=balance_data,
                headers=data.headers
            )

            if add_balance_response.status_code == 200:
                logging.info(f"Balance added successfully: {balance_data['amount']}")
                print("Balance added successfully.")
                print("Amount added:", balance_data["amount"])
            else:
                logging.error(f"Add balance failed: {add_balance_response.status_code} {add_balance_response.text}")
                print("Failed to add balance. Status code:", add_balance_response.status_code)
            break

        except requests.RequestException as e:
            logging.warning(f"Attempt {attempt + 1}: add balance request failed - {e}")
            print(e)