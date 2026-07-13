numbers = [1,2,2,3,4,4,5,1]
result = []
for n in numbers:
    if n not in result:
        result.append(n)
print("List without duplicates:", result)
# Nel, correct

fruits = ["apple", "banana", "cherry", "peach", "kiwi"]
new_fruits = []
for i in range(len(fruits)):
    if i != 0 and i != 4 and i != 5:
        new_fruits.append(fruits[i])
print("List after deleting elements:", new_fruits)
# Nel, correct

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = []
for item in list1:
    if item not in list2:
        difference.append(item)
for item in list2: # TODO,, no need this block
    if item not in list1:
        difference.append(item)
print("Difference between list1 and list2:", difference)

t = (("name", "Elmira"), ("age", 61), ("city", "Erevan"))
d = dict(t)
print("Dictionary:", d)
# Nel, correct

my_tuple = (1, 2, 3, 4, 5)
my_tuple = my_tuple + (6, 7, 8)
print("Tuple after adding elements:", my_tuple)
# Nel, correct

d={"name": "Elmira", "age": 61, "city": "Erevan"} # TODO< keep dict as i explained during lesson
d["email"] = "elmira@example.com"
print("Dictionary after adding new key-value pair:", d)

scores_dict = {"math": 90, "science": 85, "history": 88}
max_value = max(scores_dict.values())
min_value = min(scores_dict.values())
print("Maximum value in the dictionary:", max_value)
print("Minimum value in the dictionary:", min_value)
# Nel, correct

set1 = [1, 2, 3, 4, 5]
set2 = [4, 5, 6, 7, 8]
union_set = set(set1).union(set(set2))
print("Union of the two sets:", union_set)
# Nel, correct

Student_info = {
    "name": "Elmira", 
    "age": 61, 
    "city": "Erevan, Armenia",
    "education": "PhD",
    "phone numbers": ["+374 77 123456", "+37477 654321"]
}
print("Student Information:", Student_info)
print("Student Name:", Student_info["name"])
print("Phone Numbers:", Student_info["phone numbers"])
Student_info["email"] = "elmira@example.com"
print("Student Information with Email:", Student_info)
# Nel, correct

# TODO, dear Elmira, try to write once again by yourself, without any inet help