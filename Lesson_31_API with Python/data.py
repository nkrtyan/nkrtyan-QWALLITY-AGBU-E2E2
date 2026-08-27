from faker import Faker

fake = Faker()

headers = {
    "Content-Type": "application/json"
}

first_name = fake.first_name()

username = f"{first_name.lower()}_{fake.random_int(100, 999)}"

password = fake.password(length=8)

register_body = {
    "first_name": first_name,
    "email": fake.email(),
    "username": username,
    "password": password,
    "role_id": 2,
    "account": fake.random_int(min=10, max=50)
}

balance_body = {
    "amount": fake.random_int(min=100, max=1000),
    "payment": 2,
    "card_num": fake.credit_card_number(),
    "exp_date": fake.credit_card_expire(),
    "card_cvv": fake.credit_card_security_code()
}