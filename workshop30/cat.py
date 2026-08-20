from animal import Animal

class Cat(Animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height


    def showinfo(self):
        print(f"Cat Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Height: {self.height}")

class Duck(Animal):
    def __init__(self, name, age, height):
           super().__init__(name)
           self.age = age
           self.height = height


class Mouse(Animal):
     def __init__(self, name, age, height):
            super().__init__(name)
            self.age = age
            self.height = height



cat1 = Cat("Simba", 3, 5)
duck1 = Duck("Donald", 2, 10)
mouse1 = Mouse("Jerry", 1, 5)


cat1.showinfo()
cat1.move()
duck1.showinfo()
duck1.move()
mouse1.showinfo()
mouse1.move()
