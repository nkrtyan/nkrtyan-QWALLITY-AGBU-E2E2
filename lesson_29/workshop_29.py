# class Website:
#     def __init__(self, url, type):
#         self.url = url
#         self.type = type


#     def show(self):
#         print(f"Site url is {self.url}")
#         print(f"Site type is {self.type}")


# obj1 = Website("www.iuytrr.com", "Infosite")
# obj2 = Website("dfgregr.com", "buying car")

# obj1.show()
# obj2.show()

# class Food():
#     def __init__(self, fruit, color):
#         self.fruit=fruit
#         self.color=color


#     def show(self):
#         print(f"this is {self.fruit}. It is {self.color}")


# apple=Food("apple", "red")
# grape=Food("grape", "green")

# apple.show()
# grape.show()

# class MyTestClass:
  
#     some_attribute = 4   

#     def hello_world(self):
#         print("Hello World!")

# myobject = MyTestClass()

# myobject.hello_world()

# print(myobject.some_attribute)

# import math
# class Circle:
#     def __init__(self, radius):
#         self.R = radius

#     def surface(self):
#         return self.R ** 2 * math.pi

# mycircle = Circle(3)
# print(mycircle.surface())

# 

# class MyClass:
#     instance_count = 0

#     def __init__(self):
#         MyClass.instance_count += 1
#         print(MyClass.instance_count)

#     @classmethod
#     def reset_instance_count(cls):
#         print("Resetting count of instances")
#         cls.instance_count = 0

# obj1 = MyClass()
# obj2 = MyClass()
# MyClass.reset_instance_count()
# obj3 = MyClass()


class Robot:
    pass

x = Robot()
y = Robot()
x.name = "Marvin"
x.build_year = "1979"
y.name = "Caliban"
y.build_year = "1993"
print(x.name)

print(x.__dict__)
print(y.__dict__)
