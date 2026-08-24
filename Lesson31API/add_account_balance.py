import requests
import api_collection
import lesson_31


def add_account_balance(token):
    headers = {
        "Content-type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    payment_data = {
        "amount": lesson_31.BALANCE_AMOUNT,
        "payment": 1,
        "card_num": 0,
        "exp_date": "yyyy/mm/dd",
        "card_cvv": "string"
    }

    try:
        response = requests.post(
            api_collection.add_balance_endpoint,
            json=payment_data,
            headers=headers
        )

        print("Status code:", response.status_code)
        print("Response:", response.text)

        return response

    except requests.RequestException as e:
        print("Request failed:", e)


from login import test_login_user

token = test_login_user()

add_account_balance(token)