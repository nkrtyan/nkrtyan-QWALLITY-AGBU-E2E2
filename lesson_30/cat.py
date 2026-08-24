from workshop_30 import Animal


class Cat(Animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age=age
        self.height=height


    def showInfo(self):
        print(f"{self.name} is a cat. it is {self.age} years old and has {self.height} cm heigth") 


class Mouse(Animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height

    def showInfo(self):
        print(f"{self.name} is a mouse. It is {self.age} years old and has {self.height} cm height.")



class Duck(Animal):
    def __init__(self, name, age, height):
        super().__init__(name)
        self.age = age
        self.height = height

    def showInfo(self):
        print(f"{self.name} is a duck. It is {self.age} years old and has {self.height} cm height.")




obj_animal = Animal('Generic Animal')
obj_cat = Cat('Joe', 5, 30)
obj_mouse = Mouse('Jerry', 1, 10)
obj_duck = Duck('Donald', 2, 20)

obj_animal.move()
obj_cat.move()
obj_mouse.move()
obj_duck.move()

obj_animal.showInfo()
obj_cat.showInfo()
obj_mouse.showInfo()
obj_duck.showInfo()
