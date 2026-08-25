import requests
import endpoints
import data


def test_add_account_balance(headers):
    balance_data = data.balance_body

    for attempt in range(10):
        try:
            Add_account_balance_response = requests.post(
                endpoints.add_account_balance_endpoint,
                json=balance_data,
                headers=headers
            )

            if Add_account_balance_response.status_code == 200:
                print("Balance added successfully.")
                break


        except requests.RequestException as e:
            print(e)
           

    return Add_account_balance_response