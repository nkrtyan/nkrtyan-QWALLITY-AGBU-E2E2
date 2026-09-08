class Animal:
    def __init__(self, name):
        self.name = name


    def showinfo(self):
        print(f"Animal Name: {self.name}")


    def move(self):
        print(f"{self.name} is moving.")    