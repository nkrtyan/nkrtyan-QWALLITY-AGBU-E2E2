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

    
swimming_obj = Sport("Swiming", data["Swimming"]["price"], data ["Swimming"]["session"]) # TODO, i would like to see "Swimming not hard coded, get from dict.keys()"
tennis_obj = Sport("Tennis", data["Tennis"]["price"], data["Tennis"]["session"])


swimming_obj.show_data()
tennis_obj.show_data()

# TODO, alternative and more universal solution is
"""
# Get sport names
sport_names = list(data.keys())

# Create list for Sport objects
sport_objects = []

for sport in sport_names:
    sport_obj = Sport(
        sport,
        data[sport]["price"],
        data[sport]["session"]
    )

    sport_objects.append(sport_obj)


# Show information
for sport_obj in sport_objects:
    sport_obj.show_data()
"""