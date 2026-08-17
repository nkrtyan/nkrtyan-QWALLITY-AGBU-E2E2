#Option 1
# TODO, keep this format
courses = {
    "swimming": {
        "price": 40000, 
        "month": 16
        },
    "tennis": {
        "price": 50000, 
        "month": 10
        }
}


class Sport:
    def __init__(self, name, price, session):
        self.name = name
        self.price = price
        self.session = session

    def show_calculates(self):
        return self.price / self.session


swimming_obj = Sport("swimming", 40000, 16) # TODO,  do not hard code data, you should get it from dict
tennis_obj = Sport("tennis", 50000, 10) # TODO, the same here


print(f"Swimming - {swimming_obj.show_calculates()} AMD per session")
print(f"Tennis - {tennis_obj.show_calculates()} AMD per session")



#Option 2
courses = {
    "swimming": {"price": 40000, "month": 16},
    "tennis": {"price": 50000, "month": 10}
}


class Sport:
    def __init__(self, name, price, session):
        self.name = name
        self.price = price
        self.session = session
        self.per_session = price / session

    def show_calculates(self):
        return self.per_session


swimming_obj = Sport("swimming", 40000, 16)
tennis_obj = Sport("tennis", 50000, 10)

print(f"Swimming - {swimming_obj.per_session} AMD per session")
print(f"Tennis - {tennis_obj.per_session} AMD per session")

# Nel,OOP is kept, but need to correct passing data ffrom dict