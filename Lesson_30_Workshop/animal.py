class Animal:
    def __init__(self, name):
        self.name = name

    def showINFO(self):
        print("Name", self.name)

    def move(self):
        print(self.name, "is moving")
        