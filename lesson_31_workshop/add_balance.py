import requests
import endpoints
import data


def test_add_balance(headers):
    for attempt in range(10):

        try:
            add_balance_response = requests.post(endpoints.add_balance_endpoint, json=data.balance_body, headers=headers)


            if add_balance_response.status_code == 200:
                print("Balance added successfully.")
                print(add_balance_response.json())
                break

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Add balance failed. Retrying...")

    return add_balance_response