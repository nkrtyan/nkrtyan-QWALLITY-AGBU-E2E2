import requests
import endpoints
import data


def test_add_balance(headers):
    balance_data = data.balance_body

    for attempt in range(10):

        try:
            add_balance_response = requests.post(endpoints.add_balance_endpoint, json=balance_data, headers=data.headers)


            if add_balance_response.status_code == 200:
                print("Balance added successfully.")
                print(add_balance_response.json())
                break

            else:
                print("Failed to add balance. Status code:", add_balance_response.status_code)
                print("Response:", add_balance_response.text)
                


        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Add balance failed. Retrying...")

    return add_balance_response

