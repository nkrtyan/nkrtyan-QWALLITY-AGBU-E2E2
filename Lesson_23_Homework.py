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


my_numbers.pop(5) #2 Write a Python program which print a specified list after removing the 0th, 4th and     5th elements.  
my_numbers.pop(4)
my_numbers.pop(0)

print("Updated list:", my_numbers)

my_list1 = [2, 5, 3, 9, 7, 12]
my_list2 = [3, 7, 10, 12, 15]

difference = []

for number in my_list1:
    if number not in my_list2:
        difference.append(number)

print("List 1:", my_list1)
print("List 2:", my_list2)
print("Difference:", difference)

