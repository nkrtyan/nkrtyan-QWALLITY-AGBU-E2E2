# Homework Task: Sport Session Price

data= {
    "name":["Swimming", "Tennis"],
    "price": [40000, 50000],
    "number_sessions": [16, 10]
}
# TODO, keep dict like sport_1 and data (dict value, like sport_name:Swimming, price:40000, number_of_session:16)

class Sport():
    def __init__(self, name, price, number_sessions):
        self.name = name
        self.price = price
        self.number_sessions = number_sessions


    def show(self):
        print(f"{self.name} - {self.price/self.number_sessions} AMD per session")


swimming_obj=Sport(data['name'][0], data["price"][0], data["number_sessions"][0])
tennis_obj=Sport(data['name'][1], data["price"][1], data["number_sessions"][1])


swimming_obj.show()
tennis_obj.show()
# Nel,  OOP is kept, code is working correctly, just would like to see another dict

"""Create a Python program to calculate the price of one training session for different sports.
Use the following sports:
Swimming — 40,000 AMD per month, 16 sessions
Tennis — 50,000 AMD per month, 10 sessions
Requirements
Keep the sports information in a global dictionary.
Create a Sport class.
Each sport should have a name, price, and number of sessions.
Create a method that calculates the price of one session.
Create objects for swimming_obj and tennis_obj.
Print the session price for each sport.

Expected Output
Swimming - 2500.0 AMD per session
Tennis - 5000.0 AMD per session
"""