from faker import Faker
fake = Faker()

headers = {
    'Content-type': 'aplication.json'
}

register_body = {
                "first_name": fake.first_name(),
                "email": fake.email(),
                "username": fake.user_name(),
                "password": fake.password(),
                "role_id": 2,
                "account": fake.random_int(min=20, max=100)
                }

balance_body= {
                "amount": fake.random_int(min=100, max=10000),
                "payment": 2,
                "card_num": fake.credit_card_number(),
                "exp_date": fake.credit_card_expire(),
                "card_cvv": fake.credit_card_security_code()
                }