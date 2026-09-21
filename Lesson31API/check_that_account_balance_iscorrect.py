import requests
import api_collection
import lesson_31
from login import test_login_user


def check_account_balance(token):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(
            api_collection.get_balance_endpoint,
            headers=headers
        )

        print("Status code:", response.status_code)
        print("Response:", response.text)

        if response.status_code == 200:
            actual_balance = int(response.json()["balance"])

            expected_balance = 2100

            if actual_balance == expected_balance:
                print("Balance is correct!")
            else:
                print("Balance is incorrect!")
                print("Expected:", expected_balance)
                print("Actual:", actual_balance)

    except requests.RequestException as e:
        print("Request failed:", e)


token = test_login_user()

check_account_balance(token)