class Website:
    def __init__(self, url, type):
        self.url = url
        self.type = type


    def show(self):
        print(f"Site url is {self.url}")
        print(f"Site type is {self.type}")


obj1 = Website("www.iuytrr.com", "Infosite")
obj2 = Website("dfgregr.com", "buying car")

obj1.show()
obj2.show()

