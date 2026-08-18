data = {
    "Swimming": {
        "price": 40000,
        "session": 16
    },

    "Tennis": {
        "price": 50000,
        "session": 10
    }
}

class Sport:
    def __init__(self, name, price, sessions):
        self.name = name
        self.price = price
        self.sessions = sessions

    def show_data(self):
        session_price = self.price / self.sessions
        print(f"{self.name} - {session_price} AMD per session")


sport_objects = []

for sport in data.keys():

    sport_obj = Sport(
        sport,
        data[sport]["price"],
        data[sport]["session"]
    )

    sport_objects.append(sport_obj)

for sport_obj in sport_objects:
    sport_obj.show_data()

# Nel, OOP is correct, correct dict and call


