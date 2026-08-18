from animal import Animal

class Cat(Animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height

        
    def showinfo(self):
        print(f"This is cat, his name is {self.name}, he is {self.age} years old and his height is {self.height} sm")


    def get_category(self):
        if self.age<1:
            return f"{self.name} is kitten"
        elif self.age<10:
            return f"{self.name} is young cat"
        else:
            return f"{self.name} is adult cat"


if __name__ == "__main__":
    name=input("Input cat name: ")
    age = int(input("Enter age: "))
    height = int(input("Enter height: "))

    cat = Cat(name, age, height)
    cat.showinfo()
    cat.move()
    category = cat.get_category()
    print(category)