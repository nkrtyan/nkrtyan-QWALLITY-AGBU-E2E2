# Keep the sports information in a global dictionary
sport_types = {
    "Swimming": {"price": 40000, "sessions": 16},
    "Tennis": {"price": 50000, "sessions": 10}
}

sport_names = list(sport_types.keys())
#FIX, keep kson like two seperate sports, and in line 22 pass swimming like firts dict key, tennis like second key, no need hardcode swimming and tennis

# Create a Sport class
# Each sport should have a name, price, and number of sessions
class Sport:
    def __init__(self, name, price, sessions):
        self.name = name
        self.price = price
        self.sessions = sessions

    # Create a method that calculates the price of one session
    def session_price(self):
        return self.price / self.sessions


# Create objects for swimming_obj and tennis_obj
swimming_obj = Sport(sport_names[0], sport_types[sport_names[0]]["price"], sport_types[sport_names[0]]["sessions"])
tennis_obj = Sport(sport_names[1], sport_types[sport_names[1]]["price"], sport_types[sport_names[1]]["sessions"])


# Print the session price for each sport
print(f"{swimming_obj.name} - {swimming_obj.session_price()} AMD per session")
print(f"{tennis_obj.name} - {tennis_obj.session_price()} AMD per session")

# Nel, OOP is kept, only correct dict part