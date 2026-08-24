class Animal:
    def __init__ (self, name):
        self.name=name


    def showInfo(self):
        print(f"Animal is {self.name}")
                

    def move(self):
        print(f"{self.name} is running")
        

if __name__=="__main__":
    obj1= Animal("Joe")
    obj1.showInfo()
    obj1.move()
