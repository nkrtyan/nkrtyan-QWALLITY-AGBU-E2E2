my_list=[7, 9, 64, 9, 7, 8, 40, 32]
unique_numbers=[]
for number in my_list:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)

my_list = [2, 4, 6, 8, 10, 12]
del my_list[1]
del my_list[3]
del my_list[0]
print("my_list:", my_list)

my_list_1 = [3, 6, 9, 12, 15]
my_list_2 = [1, 3, 5, 7, 9]
difference_list = []
for number in my_list_1:
     if number not in my_list_2:
         difference_list.append(number)
print(difference_list)

tuple = (("name", "Diana"), ("age", 29), ("city", "Yerevan"),("education", "ISIFA"))
dict = dict(tuple)
print(dict)


tuple1 = (10, 20, 30, 40, 50)
list1 = list(tuple1)
list1.append(2)
tuple1 = tuple(list1)
print(tuple1)

tuple2 = (1, 2, 3, 4, 5)
list2 = list(tuple2)
list2.insert(0, 40)
tuple2 = tuple(list2)
print(tuple2)

 
dict_1 = {
     "name": "Diana",
     "age": 29
}
dict_1["address"] = "Baghramyan 60/1"
print(dict_1)

dict_2 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}
maximum = 0
minimum = 0
for value in dict_2.values():
     if value > maximum:
         maximum = value
     if minimum == 0 or value < minimum:
         minimum = value
print("Maximum:", maximum)
print("Minimum:", minimum)

set_1 = {5, 6, 7, 8}
set_2 = {9, 10, 11, 12}
print(set_1|set_2)

student = {
    "name": "Diana",
    "age": 29,
    "address": "Yerevan",
    "education": "ISIFA",
    "phone_numbers": [""
    "+377219751"]
}

print(student)
print(student["name"])
print(student["phone_numbers"])
student["email"] = "diana@gmail.com"
print(student)