"""#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)

#2 Write a Python program which print a specified list after removing the 0th, 4th and     5th elements.  

#3 Write a Python program to get the difference between the two lists.

#4 Write a Python program to convert a tuple to a dictionary.

#5 Write a Python program to add an item in a tuple.

#6 Write a Python program to add a key with value to a dictionary.

#7 Write a Python program to get the maximum and minimum value in a dictionary().

#8 Write a Python program to create a union of sets.

#9 Student  Information
Write a Python program to create a dictionary with the following information about a student:
•	name 
•	age 
•	address 
•	education 
•	phone_numbers (store two phone numbers in a list) 
Then:
1.	Print the entire dictionary. 
2.	Print only the student's name. 
3.	Print only the list of phone numbers. 
4.	Add a new key called "email" with your email address. 
5.	Print the updated dictionary."""

my_numbers = [2, 5, 3, 9, 7, 5, 2, 12, 9, 25, 38, 25, 49]

unique_numbers = [] #1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)

for number in my_numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original list:", my_numbers)
print("List without duplicates:", unique_numbers)
#Nel, correct


my_numbers.pop(5) #2 Write a Python program which print a specified list after removing the 0th, 4th and     5th elements.  
my_numbers.pop(4)
my_numbers.pop(0)

print("Updated list:", my_numbers)
#Nel, correct

my_list1 = [2, 5, 3, 9, 7, 12] #3 Write a Python program to get the difference between the two lists.
my_list2 = [3, 7, 10, 12, 15]

difference = []

for number in my_list1:
    if number not in my_list2:
        difference.append(number)
for number in my_list2: # TDSO, this part is additional
    if number not in my_list1:
        difference.append(number)

print("List 1:", my_list1)
print("List 2:", my_list2)
print("Difference:", difference)

my_tuple = (("name", "Kristine"), #Write a Python program to convert a tuple to a dictionary.
            ("age", 38),
            ("city", "Yerevan"))

my_dict = {}
#Nel, correct

for item in my_tuple:
    key = item[0]
    value = item[1]
    my_dict[key] = value

print("Tuple:", my_tuple)
print("Dictionary:", my_dict)
#Nel, correct

my_tuple = (2, 5, 3, 9) #Write a Python program to add an item in a tuple.
new_item = 7
my_tuple = my_tuple + (new_item,)

print("Updated tuple:", my_tuple)
#Nel, correct

my_dict = {  #Write a Python program to add a key with value to a dictionary
    "name": "Kristine",
    "age": 38,
    "city": "Yerevan"
}

my_dict["University"] = "Polytechnic"
print("Updated dictionary:", my_dict)
#Nel, correct

my_dict = { #Write a Python program to get the maximum and minimum value in a dictionary().
    "a": 15,
    "b": 7,
    "c": 25,
    "d": 3,
    "e": 18
}

values = list(my_dict.values())

maximum = values[0]
minimum = values[0]

for value in values:
    if value > maximum:
        maximum = value

    if value < minimum:
        minimum = value

print("Dictionary:", my_dict)
print("Maximum value:", maximum)
print("Minimum value:", minimum)

#Nel,just call max() and min()

set1 = {2, 5, 3, 9} #Write a Python program to create a union of sets.
set2 = {7, 3, 5, 12}

union_set = set1.union(set2)
print("Union:", union_set)
#Nel, correct


student = {
    "name": "Kristine Ghukasyan",
    "age": 38,
    "address": "Yerevan",
    "education": "National Polytechnic University of Armenia",
    "phone_numbers": ["093341485", "096341485"]
}

#1. Print the entire dictionary
print("Student Information:")
print(student)

#2. Print only the student's name
print("Name:", student["name"])

#3. Print only the list of phone numbers
print("Phone Numbers:", student["phone_numbers"])

#4. Add a new key called "email"
student["email"] = "kristinetigra@gmail.com"

#5. Print the updated dictionary
print("Updated Dictionary:")
print(student)
#Nel, correct