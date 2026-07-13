1
elements = [1, 2, 3, 2, 5, 1, 7, 10, 5, 2, 10, 25, 4]
elements.sort()
elements1 = [elements[0]]
for item in elements:
    if item != elements1[-1]:
        elements1.append(item)
print(elements1)


2
list = ['White', 'Red', 'Green', 'Black', 'Yellow', 'Pink', 'Blue']
result_list = []
for i in range(len(list)):
    if i != 0 and i != 4 and i != 5:
        result_list.append(list[i])
print(result_list)


3
list_1 = [10, 20, 30, 40, 50, 60]
list_2 = [5, 10, 15, 20, 25, 30, 35, 40]
difference_list = []
for item_1 in list_1:
    if list_2.count(item_1) == 0:
        difference_list.append(item_1)
print(difference_list)


4
list = ["a", "b", "c", "d", "e"]
odd_list = []
for i in range(len(list)):
    if i % 2 != 0:
        odd_list.append(list[i])
print(odd_list)


5
list_3d = []
for i in range(3):
    row_2d = []
    for j in range(4):
        column_1d = []
        for k in range(6):
            column_1d.append ("*")
        row_2d.append(column_1d)
    list_3d.append(row_2d)
print(list_3d)


6
letters = ['a', 'd', 'd', 'r', 'e', 's', 's']
result_text = "".join(letters)
print(result_text)


7
test_list = []
if len(test_list) == 0:
    print("List is empty")
else:
    print("List is not empty")


8
my_list = [10, 21, 32, 43, 54, 65]
copied_list = []
for item in my_list:
    copied_list.append(item)
print("Copied list:", copied_list)
   
    
    
9
student = {
    "name": "Syuzanna",
    "surname": "Stepanyan",
    "age": 45,
    "address": "Tigran Mets",
    "education": "Master Degree",
    "phone_numbers": ["+37455185457","+37477856545"]
    }
print(student)
print(student["name"])
print(student["phone_numbers"])
student["email"] = "stepanyan@gmail.com"
print(student)