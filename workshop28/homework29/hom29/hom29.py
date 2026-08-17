dict_price = {
    "name": ["swimming" , "tennis"],
    "month":[40000 , 50000],
    "sessions":[16 , 10]
}
class Sports:

    def __init__(self, price, number, sessions):
        self.price = price
        self.number = number
        self.sessions = sessions

    def calculate_session(self):
        return self.price/self.sessions

swimming_obj = Sports(dict_price["month"][0], 1,  dict_price["sessions"][0])
tennis_obj = Sports(dict_price["month"][1], 2,  dict_price["sessions"][1])


print(f"Swimming session price: {swimming_obj.calculate_session()}")
print(f"Tennis session price: {tennis_obj.calculate_session()}")