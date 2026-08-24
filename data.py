from faker import Faker
fake = Faker()

headers = {""
    "content-type": "application/json"
}

registor_body ={

  "first_name": fake.first_name(),
  "email": fake.email(),
  "username": fake.user_name(),
  "password": fake.password(length=8),
  "role_id": 2,
  "account": fake.random_int(min = 20, max= 100)
}



login_body = {
    "username": registor_body["username"],
    "password": registor_body["password"]
}

balance_body = {
    "amount": 100,
    "payment": "1",
    "card_num": 0,
    "exp_date": "2026/12/31",
    "card_cvv": "123"
}