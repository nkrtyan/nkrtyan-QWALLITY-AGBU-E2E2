

from faker import Faker

fake = Faker()

headers = {
    'Content-Type': 'application/json'
}

def register_body():
    return {
        "first_name": fake.first_name(),
        "email": fake.email(),
        "username": fake.user_name(),
        "password": fake.password(length=8),
        "role_id": 2,
        "account": fake.random_int(min=20, max=100)
    }

balance_body = {
    "account": 50,         
    "amount": 100,         
    "payment_method": "Cash"
}