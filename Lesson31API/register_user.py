import requests
import api_collection
import lesson_31


def test_register_user():
    register_data = {
        "first_name": lesson_31.FIRST_NAME,
        "email": lesson_31.EMAIL,
        "username": lesson_31.USERNAME,
        "password": lesson_31.PASSWORD,
        "role_id": lesson_31.ROLE_ID,
        "account": lesson_31.ACCOUNT
    }

    username = register_data["username"]
    password = register_data["password"]

    for attempt in range(10):
        try:
            register_user_response = requests.post(
                api_collection.register_endpoint,
                json=register_data,
                headers=lesson_31.headers
            )

            if register_user_response.status_code in [200, 201]:
                print("User registered successfully!")
                print(register_user_response.json())
                print("Username -", username)
                print("Password -", password)

                return username, password

            else:
                print(
                    "Failed to register user. Status code:",
                    register_user_response.status_code
                )
                print("Response:", register_user_response.text)
                break

        except requests.RequestException as e:
            print(e)
            print(
                f"Attempt {attempt + 1}: Register failed. Retrying..."
            )


test_register_user()