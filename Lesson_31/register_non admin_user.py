import endpoints
import data
import requests


def test_register_non_admin_user():
    register_data = data.register_body
    username = register_data["username"]
    password = register_data["password"]

    for attempt in range(10):
        try:
            register_non_admin_user_response = requests.post(
                endpoints.register_endpoint,
                json=register_data,
                headers=data.headers
            )

            if register_non_admin_user_response.status_code == 201:
                print("User registered successfully!")
                print(register_non_admin_user_response.json())
                print("Username -", username)
                print("Password -", password)

                return username, password


            break

        except requests.RequestException as e:
            print(e)

    return username, password


test_register_non_admin_user()