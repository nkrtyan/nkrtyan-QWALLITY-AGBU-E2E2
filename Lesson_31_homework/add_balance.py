import requests
import endpoints
import data


def test_add_balance(headers):
    for attempt in range(10):
        try:
            response = requests.post(
                endpoints.add_balance_endpoint,
                json=data.balance_body,
                headers=headers
            )

            if response.status_code == 200 or response.status_code == 201:
                print("Balance added successfully!")
                return response

            else:
                print(
                    "Failed to add balance. Status code:",
                    response.status_code
                )
                print("Response:", response.text)
                break

        except requests.RequestException as e:
            print(e)
            print(f"Attempt {attempt + 1}: Add balance failed. Retrying...")

    return None