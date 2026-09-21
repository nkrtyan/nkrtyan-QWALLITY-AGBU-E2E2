class Website:
    def __init__(self, type , url):
        self.type = type
        self.url = url


    def print_data(self):
        print(f"Website is created, type is {self.type} ,{self.url}")   


job= Website("յօb" , "www.job.com")
job.print_data()



  
data = {
    "Name": ["Swimming", "Tennis", ],
    "Price": [40000, 50000],
    "Number": [16, 10]
}


class sport:
    def __init__(self,name,price,number ):
        self.name=name
        self.price=price
        self.number= number


    def session_price(self):
        return self.price/self.number


swimming_obj = sport (
 data ["Name"] [0],
 data ["Price"] [0],
 data ["Number"][0],
)


tennis_obj = sport (
 data ["Name"] [1],
 data ["Price"] [1],
 data ["Number"][1],
)


print(f"{swimming_obj.name} - {swimming_obj.session_price()} AMD per session")
print(f"{tennis_obj.name}   -  {tennis_obj.session_price()}  AMD per session")