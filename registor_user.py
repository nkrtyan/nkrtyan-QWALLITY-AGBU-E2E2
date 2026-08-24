import requests
import Endpoint
import data

def test_registor_user():
    registor_response = requests.post(
        Endpoint.registor_endpoint,
        json=data.registor_body,
        headers=data.headers
    )
    print("1. Registor Status:", registor_response.status_code)
    assert registor_response.status_code in [200, 201], "Registration failed"