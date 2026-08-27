from faker import Faker

fake = Faker()

headers = {
    'Content-Type': 'application/json'
}

register_body = {
    "first_name": fake.first_name(),
    "email": fake.email(),
    "username": fake.user_name(),
    "password": fake.password(length=8),
    "role_id": 2,
    "account": fake.random_int(min=20, max=100)
}

add_amount = {
                "amount": 100,
                "payment": "cash",
                "card_num": 0,
                "exp_date": "2028/08/28",
                "card_cvv": "888"
}
