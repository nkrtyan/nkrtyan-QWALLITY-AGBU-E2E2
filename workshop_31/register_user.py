import data
import endpoints
import requests


def test_register_user():
    register_data = data.register_body
    username = register_data["username"]
    password = register_data["password"]

    for attempt in range(10):
        try:
            register_user_response = requests.post(endpoints.register_endpoint, json=register_data, headers=data.headers)

            if register_user_response:
                if register_user_response.status_code == 200:
                    print("User registered successfully")
                    print(register_user_response.json())
                    print("Username -" ,username)
                    print("Password -" ,password)

                    return username, password

                else:
                    print("Registration is failed. Status code: " ,register_user_response.status_code)
                    print("Registration response: " ,register_user_response.text)

                break

        except requests.RequestException as e:
            print(e)
            print (f"Attemt {attempt + 1}: Register failed. Trying... ")

    return None, None

# test_register_user()

