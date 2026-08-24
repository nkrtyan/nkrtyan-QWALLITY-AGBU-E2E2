from faker import Faker
fake = Faker()

headers = {
    "Content-type": "application/json"
}

register_body = {
                "first_name": fake.first_name(),
                "email": fake.email(),
                "username": fake.user_name(),
                "password": fake.password(),
                "role_id": 2,
                "account": fake.random_int(min=20, max=100)
}

course_body = {
            "title": "Python26",
            "body": "New edition",
            "coursetype": "2",
            "author": "admin_user",
            "price": 50
}