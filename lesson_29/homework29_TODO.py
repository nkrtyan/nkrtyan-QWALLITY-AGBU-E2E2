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

class Sport():
    def __init__(self, name, price, number_sessions):
        self.name = name
        self.price = price
        self.number_sessions = number_sessions


    def show(self):
        print(f"{self.name} - {self.price/self.number_sessions} AMD per session")

swimming_obj=Sport(sports.values, sports.keys["price"], sports.keys["number_sessions"])
# tennis_obj=Sport(data['name'][1], data["price"][1], data["number_sessions"][1])


swimming_obj.show()
# tennis_obj.show()