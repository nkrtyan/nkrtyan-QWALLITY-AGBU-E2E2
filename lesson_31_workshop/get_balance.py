import endpoints
import json
import requests

def test_get_balance(headers):
    for attempt in range(10):

        try:
            get_balance_response = requests.get(endpoints.get_balance_endponit, headers=headers)

            if get_balance_response:
                all_found_balances = json.loads(get_balance_response.text)

                for i in all_found_balances["result"]:
                    if int() == i["id"]:
                        print("text")
                        break
                break
        except requests.RequestException:
            print(f'Attempt {attempt + 1}: Login failed. Retrying...')