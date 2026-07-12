#During program creation create your own list, tuple, dict, set.

#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)"""
print("1.")
countries = ["Armenia", "Russia", "Japan", "France", "Armenia", "Russia"]
distinct_countries = []

for i in countries:
    if i not in distinct_countries:
        distinct_countries.append(i)

print("All countries-", countries)
print("Distinct Countries-", distinct_countries)

#2 Write a Python program which print a specified list after removing the 0th, 4th and     5th elements.  
print("2.")
countries = ["Armenia", "Russia", "Japan", "France", "Armenia", "Russia"]
del countries [5]
del countries [4]
del countries [0]
print(countries)

#3 Write a Python program to get the difference between th
#e two lists.
print("3.")
list_1 = [1, 2, 3, 4, 5,]
list_2 = [4, 5, 6, 2, 1, 7, 8,]
difference = set(list_2) - set(list_1)
print(difference)

#4 Write a Python program to convert a tuple to a dictionary.
print("4.")
student_tuple = ("name", "Poghos", "age", 35, "city", "Yerevan")
student_dict = {}

for i in range(0, len(student_tuple), 2):
    student_dict[student_tuple[i]] = student_tuple[i + 1]

print("Tuple:", student_tuple)
print("Dictionary:", student_dict)

#5 Write a Python program to add an item in a tuple.
print("5.")
my_tuple = ("Poghos", "Petros", "Martiros", 2026)
updated_tuple = list(my_tuple)
updated_tuple.append("Baghdasar")
print(tuple(updated_tuple))

#6 Write a Python program to add a key with value to a dictionary.
print("6.")
my_car={
    "brand":"Mersedes",
     "color":"white"
}
my_car["year"]= 2000
print(my_car)


#7 Write a Python program to get the maximum and minimum value in a dictionary().
print("7.")
exam_results = {"Ani": 88, "Davit": 74, "Mariam": 91, "Sona": 67}

print("Dictionary:", exam_results)
print("Maximum value:", max(exam_results.values()))
print("Minimum value:", min(exam_results.values()))

#8 Write a Python program to create a union of sets.
print("8.")
animals = {"dog", "cat", "elephant", "sparrow"}
birds = {"sparrow", "eagle", "parrot"}
union_result = animals.union(birds)

print("Animals:", animals)
print("Birds:", birds)
print("Union:", union_result)


"""#9 Student  Information
Write a Python program to create a dictionary with the following information about a student:
name 
age 
address 
education 
phone_numbers (store two phone numbers in a list) 
Then:
Print the entire dictionary. 
Print only the student's name. 
Print only the list of phone numbers. 
Add a new key called "email" with your email address. 
Print the updated dictionary."""

print("9.")
student_info = {
    "name":"Ani",
    "age": 20,
    "addres":"Yerevan",
    "education":"YSU",
    "phone":("077123456","1234")
}
print("Student information", student_info)
print("Student name", student_info["name"])
print("Phone numbers", student_info["phone"])
student_info["email"] = "ani@gmail.com"
print("Updated student information", student_info)




