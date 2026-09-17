from faker import Faker
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='homework_31.log',
    filemode='a',
    encoding='utf-8')



fake = Faker()

headers = {
    "Content-Type": "application/json"
}

register_body = {
    "first_name": fake.first_name(),
    "email": fake.email(),
    "username": fake.user_name(),
    "password": fake.password(length=8),
    "role_id": 2,
    "account": fake.random_int(min=20, max=100)
}


add_balance_body = {
    "amount": fake.random_int(min=10, max=200),
    "payment": 1,
    "card_num": fake.credit_card_number(),
    "exp_date": fake.credit_card_expire(date_format="%Y/%m/%d"),
    "card_cvv": fake.credit_card_security_code()
}

