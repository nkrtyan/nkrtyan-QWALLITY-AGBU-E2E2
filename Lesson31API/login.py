import requests
import api_collection
import lesson_31


def test_login_user():
    login_data = {
        "username": lesson_31.USERNAME,
        "password": lesson_31.PASSWORD
    }

    print("Username:", lesson_31.USERNAME)
    print("Password:", lesson_31.PASSWORD)

    try:
        response = requests.post(
            api_collection.login_endpoint,
            json=login_data,
            headers=lesson_31.headers
        )

        print("Status code:", response.status_code)
        print("Response:", response.text)

        if response.status_code == 200:
            print("Login successful!")

            token = response.json()["token"]
            print("Token:", token)

            return token

    except requests.RequestException as e:
        print("Request failed:", e)


test_login_user()