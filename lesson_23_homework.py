#1 Write a program to remove duplicates from a list(write logic of the set, do not use set)

my_list = [1, 2, 3, 4, 5, 1, 5, 8]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item) 
print(unique_list, "\n") 
# Nel, correct

#2 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.  
clean_list = []
for index in range(len(my_list)):
    if index != 0 and index != 4 and index != 5:
        clean_list.append(my_list[index])
my_list = clean_list
print(my_list, "\n")
# Nel, correct

#3 Write a Python program to get the difference between the two lists
list1 = ["apple", "banana", "cherry", "orange", "kiwi"]
list2 = ["banana", "grapes", "kiwi", "mango", "apple"]
difference = []
for item in list1:
    if item not in list2:
        difference.append(item)
print(difference, "\n")
# Nel, correct, you think why you dont use set here :)

#4 Write a Python program to convert a tuple to a dictionary.
tuple = (("apple", 3), ("banana", 5), ("cherry", 2))
dictionary = dict(tuple)
print(dictionary, "\n")
# Nel, correct

#second way 
tuple_data = (("name", "Meri"), ("age", 22), ("education", "NUACA"))
new_data = {}
for key, value in tuple_data:
    new_data[key]=value
print(new_data, "\n")
# Nel, correct

#5 Write a Python program to add an item in a tuple.
my_tuple = ("red", "green", "blue")
new_list = list(my_tuple)
new_list.append("yellow")
my_tuple = new_list
print(my_tuple, "\n")
# Nel, correct

#6 Write a Python program to add a key with value to a dictionary.
my_dic = {
    "username": "admin112",
    "email": "admin@gmail.com",
}

my_dic["phone"]="099665544"
print(my_dic, "\n")
# Nel, correct

#7 Write a Python program to get the maximum and minimum value in a dictionary().
ages = {"Maria": 24, "Aram": 30, "Anahit": 18, "Dianna": 20}
max_value = max(ages.values())
min_value = min(ages.values())
print("Youngest person age:", max_value)  
print("Eldest person age:", min_value, "\n")
# Nel, correct

#8 Write a Python program to create a union of sets.
my_set1 = {1, 2, 3, 4, 4, 5}
my_set2 = {9, 3,  4, 7, 6}
my_set = my_set1 | my_set2
print(my_set, "\n")
# Nel, correct

# #9 Student  Information
# Write a Python program to create a dictionary with the following information about a student:
# name 
# age 
# address 
# education 
# phone_numbers (store two phone numbers in a list) 
# Then:
# Print the entire dictionary. 
# Print only the student's name. 
# Print only the list of phone numbers. 
# Add a new key called "email" with your email address. 
# Print the updated dictionary.

student = {
    "name": "Ani",
    "age": 25,
    "address": "Komitas", 
    "education": "Bachelor's degree", 
    "phone_numbers": ["099663355", "077889944"]  
}
print(student)
print(student["name"])
print(student["phone_numbers"])
student["email"]="ani@gmail.com"
print(student)
# Nel, correct
# greate job