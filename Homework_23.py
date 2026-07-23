my_list=[7, 9, 64, 9, 7, 8, 40, 32]
unique_numbers=[]
for number in my_list:
    if number not in unique_numbers:
        unique_numbers.append(number)
print(unique_numbers)
# Nel, correct

my_list = [2, 4, 6, 8, 10, 12]
del my_list[5]
del my_list[3]
del my_list[0]
print("my_list:", my_list)
# TODO, would be  better to remove from the end of the list
# Corrected version:

my_list_1 = [3, 6, 9, 12, 15]
my_list_2 = [1, 3, 5, 7, 9]
difference_list = []
for number in my_list_1:
     if number not in my_list_2:
         difference_list.append(number)
print(difference_list)
# Nel, correct

tuple = (("name", "Diana"), ("age", 29), ("city", "Yerevan"),("education", "ISIFA"))
dict = dict(tuple)
print(dict)
# Nel, correct


tuple1 = (10, 20, 30, 40, 50)
list1 = list(tuple1)
list1.append(2)
tuple1 = tuple(list1)
print(tuple1)
# Nel, correct

tuple2 = (1, 2, 3, 4, 5)
list2 = list(tuple2)
list2.insert(0, 40)
tuple2 = tuple(list2)
print(tuple2)
# Nel, correct

 
dict_1 = {
     "name": "Diana",
     "age": 29
}
dict_1["address"] = "Baghramyan 60/1"
print(dict_1)
# Nel, correct

dict_2 = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}
max = 0
min = 0
for value in dict_2.values():
     if value > max:
         max = value
     if min == 0 or value < min:
         min = value
print("Maximum:", max)
print("Minimum:", min)
# TODO, just call max(),min() functions
# Corrected version:

set_1 = {5, 6, 7, 8}
set_2 = {9, 10, 11, 12}
print(set_1|set_2)
# Nel, correct

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
# Nel, correct