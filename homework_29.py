# Keep the sports information in a global dictionary
sport_types = {
    "Swimming": {"price": 40000, "sessions": 16},
    "Tennis": {"price": 50000, "sessions": 10}
}
#TODO, keep kson like two seperate sports, and in line 22 pass swimming like firts dict key, tennis like second key, no need hardcode swimming and tennis

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
swimming_obj = Sport("Swimming", sport_types["Swimming"]["price"], sport_types["Swimming"]["sessions"])
tennis_obj = Sport("Tennis", sport_types["Tennis"]["price"], sport_types["Tennis"]["sessions"])

# Print the session price for each sport
print(f"{swimming_obj.name} - {swimming_obj.session_price()} AMD per session")
print(f"{tennis_obj.name} - {tennis_obj.session_price()} AMD per session")

# Nel, OOP is kept, only correct dict part