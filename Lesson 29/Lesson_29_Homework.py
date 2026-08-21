sports = {
    "Swimming": {
        "price": 40000,
        "sessions": 16
    },
    "Tennis": {
        "price": 50000,
        "sessions": 10
    }
}


class Sport:
    def __init__(self, name, price, sessions):
        self.name = name
        self.price = price
        self.sessions = sessions

    def session_price(self):
        return self.price / self.sessions

    def show(self):
        print(f"{self.name} - {self.session_price()} AMD per session")


swimming_obj = Sport(
    "Swimming", # TODO,  remove hard code, you should get it from sports dict using sports.keys()
    sports["Swimming"]["price"],
    sports["Swimming"]["sessions"]
)

tennis_obj = Sport(
    "Tennis", # TODO,  remove hard code, you should get it from sports dict using sports.keys()
    sports["Tennis"]["price"],
    sports["Tennis"]["sessions"]
)


swimming_obj.show()
tennis_obj.show()
# Nel, OOP is kept, working code