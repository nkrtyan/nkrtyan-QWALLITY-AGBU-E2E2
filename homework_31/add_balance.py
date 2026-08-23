import requests
import data
import endpoints


def test_add_balance():
    response = requests.post(
        endpoints.add_balance_endpoint,
        json=data.add_balance_body,
        headers=data.headers
    )

    assert response.status_code == 200

    print("Balance added successfully.")
    print("Amount added:", data.add_balance_body["amount"])