from animal import Animal


class Cat(Animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height

    def showINFO(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Height:", self.height)
        print("Type: Cat")

    def move(self):
        print(self.name, "is walking")