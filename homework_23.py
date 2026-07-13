# 1.  Write a Python program to remove duplicates from a list(write logic of the set, do not use set)
print()
list_with_duplicates = [1, 2, 3, 2, 4, 5, 1, 6, 3]
unique_list = []
for item in list_with_duplicates:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

# 2. Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.
print()
list = [1, 2, 3, 4, 5]
del list[4]
del list[3]
del list[0]
print(list)

# 3. Write a Python program to get the difference between the two lists.
print()
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = list(set(list1) - set(list2))
print(difference) 

#4. Write a Python program to convert a tuple to a dictionary.
print()
tuple_data = (('a', 1), ('b', 2), ('c', 3))
dictionary_data = dict(tuple_data)
print(dictionary_data)


#5 Write a Python program to add an item in a tuple.
print
tuple = (1, 2, 3)
new_item = 4
tuple = tuple + (new_item,)
print(tuple)


#6 Write a Python program to add a key with value to a dictionary.
print()
dictionary = {'a': 1, 'b': 2}
dictionary['c'] = 3
print(dictionary)


#7 Write a Python program to get the maximum and minimum value in a dictionary().
print()
dictionary = {'a': 1, 'b': 2, 'c': 3}
max_value = max(dictionary.values())
min_value = min(dictionary.values())
print("Maximum value:", max_value)
print("Minimum value:", min_value)


#8 Write a Python program to create a union of sets.
print()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)


#9 Student  Information
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
print()
student_info ={
    "name": "Hripsime",
    "age": 20,
    "address": "Yerevan, Armenia",
    "education": "Bachelor's Degree",
    "phone_numbers": ["123-456-7890", "098-765-4321"]
}
print(student_info)
print("Student's name:", student_info["name"])
print("Phone numbers:", student_info["phone_numbers"])
student_info["email"] = "hripsime.babayan@example.com"
print(f"Updated dictionary: {student_info}\n")