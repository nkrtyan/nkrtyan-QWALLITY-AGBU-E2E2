sports = {
    "name":["Swimming","Tennis"],
    "price": [40000, 50000],
    "sessions": [16, 10]
}
# TODO, make dict like each sport as separate pair, like name: tennis, price: 40000. session: 16

class Sport:
    def __init__(self, name, price, sessions):
        self.name = name
        self.price = price
        self.sessions = sessions

    def session_price(self):
        return self.price / self.sessions


swimming_obj = Sport("Swimming", 40000, 16) # TODO, do not hardcode data during object creation, you should get data from dict
tennis_obj = Sport("Tennis", 50000, 10)

print(f"{swimming_obj.name} - {swimming_obj.session_price()} AMD per session")
print(f"{tennis_obj.name} - {tennis_obj.session_price()} AMD per session")
# Nel, OOP is kept, but dict and data passing are incorrect