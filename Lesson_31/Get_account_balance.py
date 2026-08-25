import endpoints
import requests
import data


def test_Get_account_balance(headers):
    for attempt in range(10):

        try:
            Get_account_balance_response = requests.get(
                endpoints.get_account_balance_endpoint,
                headers=headers
            )

            if Get_account_balance_response.status_code == 200:
                response_data = get_account_balance_response.json()
                actual_balance = response_data.get("balance")

                print("Successfully got the balance!")

                break


        except requests.RequestException as e:
            print(e)