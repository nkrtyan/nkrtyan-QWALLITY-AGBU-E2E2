# my_list=[5,6,87,5,90,6]
# uniq_number=[]
# for number in my_list:
#     if number not in uniq_number:
#         uniq_number.append(number)
# print(uniq_number)

# my_list = [10,20,30,40,50,80,101]
# del my_list[5]
# del my_list[4]
# del my_list[0]
# print("my_list:", my_list)

# list_1 = [100, 252, 3, 4, 10]
# list_2 = [3, 100, 4, 5, 6]
# new_list = []
# for number in list_1:
#     if number not in list_2:
#         new_list.append(number)
# print(new_list)

# my_tuple = (("name", "Gayane"), ("age", 35), ("city", "Yerevan"),("education", "YSU"))
# my_dict = dict(my_tuple)
# print(my_dict)

# for the 5th task, i used two approaches
# my_tuple = (1, 2, 3,15,36)
# my_list = list(my_tuple)
# my_list.append(4)
# my_tuple = tuple(my_list)
# print(my_tuple)

# my_tuple = (10, 20, 30, 40)
# my_list = list(my_tuple)
# my_list.insert(3, 99)
# my_tuple = tuple(my_list)
# print(my_tuple)

# my_dict = {
#     "name": "Gayane",
#     "age": 35
# }
# my_dict["adress"]="Sofiayi 60/1"
# print(my_dict)

my_dict = {
    "a": 10,
    "b": 5,
    "c": 20,
    "d": 3
}
# maximum = 0
# minimum = 0
# for value in my_dict.values():
#     if value > maximum:
#         maximum = value
#     if minimum == 0 or value < minimum:
#         minimum = value
# print("Maximum:", maximum)
# print("Minimum:", minimum)

# set_1 = {10, 2, 3, 4}
# set_2 = {3, 40, 5, 6}
# print(set_1|set_2)

student = {
    "name": "Gayane",
    "age": 35,
    "address": "Yerevan",
    "education": "YSU",
    "phone_numbers": [""
    "+37493933918", "987654321"]
}

print(student)
print(student["name"])
print(student["phone_numbers"])
student["email"] = "gayane@example.com"
print(student)