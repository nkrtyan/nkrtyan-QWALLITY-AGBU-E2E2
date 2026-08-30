class Animal:
    def __init__(self, name):
        self.name = name


    def showinfo(self):
        print(f"Animal Name: {self.name}")


class Cat(Animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height


    def showinfo(self):
        print(f"cat-> Name")
        