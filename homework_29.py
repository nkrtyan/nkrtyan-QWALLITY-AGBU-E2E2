data = {
    "Swimming": {"price": 40000, "session": 16},
    "Tennis": {"price": 50000, "session": 10}
}


class Sport:
    def __init__(self, name, price, sessions):
        self.name = name
        self.price = price
        self.sessions = sessions


    def show_data(self):
        print(f"{self.name} - {self.price / self.sessions} AMD per session") 

    
swimming_obj = Sport("Swiming", data["Swimming"]["price"], data ["Swimming"]["session"])
tennis_obj = Sport("Tennis", data["Tennis"]["price"], data["Tennis"]["session"])


swimming_obj.show_data()
tennis_obj.show_data()