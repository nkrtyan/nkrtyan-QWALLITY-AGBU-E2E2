sport_dic ={
    "swimming":{
        "price": 40000,
        "sessions": 16
},
    "tennis":{
        "price":50000,
        "sessions":10
    }
}

class Sport:
    def __init__(self,name, price, sessions):
        self.name = name
        self.price = price
        self.session = sessions


    def onesession(self):
        onesession = self.price / self.session
        return(onesession)

swimming_object = Sport(
    "swimming", # TODO, do not hardcode swimming, get this data from dict
    sport_dic  ["swimming"] ["price"],
    sport_dic  ["swimming"] ["sessions"],
)

tennis_object = Sport(
    "tennis", # TODO, do not hardcode swimming, get this data from dict
    sport_dic["tennis"] ["price"],
    sport_dic["tennis"] ["sessions"]
)

print(swimming_object.onesession())
print(tennis_object.onesession())
# Nel, OOP is kept, code is working correctly