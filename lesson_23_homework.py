#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
# Nel, correct

#2 Write a Python program which print a specified list after removing the 0th, 4th and     5th elements.  
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
my_list.remove(my_list[5])# TODO, should be 4
my_list.remove(my_list[4]) # TODO, should be 3
my_list.remove(my_list[0])
print(my_list)
# Nel, correct

#3 Write a Python program to get the difference between the two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
diff = []
for item in list1:
    if item not in list2:
        diff.append(item)
print(diff)
# Nel, correct

#4 Write a Python program to convert a tuple to a dictionary.
my_tuple = (("name", "Lia"), ("age", 20))
my_dict = dict(my_tuple)
print(my_dict)
# Nel, correct

#5 Write a Python program to add an item in a tuple.
my_tuple = ("my", "name", "lia")
new_list = list(my_tuple)
new_list.append("hello")
my_tuple = new_list
print(my_tuple)
# Nel, correct

#6Write a Python program to add a key with value to a dictionary.
my_dict = {"name": "Lia"}
my_dict["age"] = 20
print(my_dict)
# Nel, correct

#7 Write a Python program to get the maximum and minimum value in a dictionary().
data = {"a": 10, "b": 50, "c": 5}
print("Max:", max(data.values()))
print("Min:", min(data.values()))
# Nel, correct

#8 Write a Python program to create a union of sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)
# Nel, correct

#9 Student  Information.Write a Python program to create a dictionary with the following information about a student:
dict9={
    "name": "Lia",
    "surname": "Amiraghyan",
    "address": "Ijevan",
    "education": "YSU",
    "phone numbers": ["077737607", "098704569", "094258945"] 
    }
print(dict9)
print(dict9["name"])
print(dict9["phone numbers"])
dict9["email"]="amiraghyanlia@gmail.com"
print(dict9)
# Nel, correct