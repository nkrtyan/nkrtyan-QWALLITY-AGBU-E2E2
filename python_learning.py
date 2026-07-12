# var="extension"
# print(type(var))
# x=5
# x/=2
# print(x)
# mystring="This is text string"
# # print(mystring[:-2])
# var1="Elya"
# # var2="Karapetyan"
# # print(var1[0:2] + " " + var2[-10:-8])
# string8="Python"
# print(string8*3)
# name=input("Enter your name: ")
# age=input("Enter your age: ")
# print(f"Hello. My name is {name}. I am {age} years old")
#count()
from shlex import join


# text="Python is a programming language"
# print(text.count("a"))
# print(text.count("a", 0, 15))
#find
# print(text.find("y"))
#replace
# print(text.replace("Python", "Java"))
# newtext=text.replace("Python", "Java")
# print(newtext)
#reversed
# string9="Karapetyan Elya Hrayr"
# print(" ".join(reversed(string9)))
# # print(string9.split("l"))
# # x=string9.lower()
# # print(x)
# # print("?" .join(string9))
# print(len(string9))
# a="123"
# b="".join(reversed(a))
# print(f"I have {b} books")
# x=8
# y=3
# # print((x + y)**2)
# print(f"({x} + {y}) ^ 2 = {(x + y)**2}")
# x = 2.5 
# y = 13.75
# gumar1=int(x)+ int(y)
# print("".join(reversed(str(gumar1))))
# anything=[5, "words", 3.14]
# # print(anything[0])
# # anything.append("new")
# print(anything)
# # anything.remove(3.14)
# # print(anything)
# if 3.14 in anything:
#     print("Yes")
# anything[0]='new word'
# print("list updated : ")
anything=[5, "words", 3.14]
anything.insert(1, "new")
print(anything)
# print(anything[-1])
# for item in anything:
#     print(item, end=" ")
print(anything[::-1])