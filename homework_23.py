#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)
my_list=["apple", "kiwi", "mango", "apple", "banana"]
my_list2=[]
for item in my_list:
    if item not in my_list2:
        my_list2.append(item)
print(my_list2)
# Nel, correct

#2 Write a Python program which print a specified list after removing the 0th, 4th and  5th elements.  
#1st solution
my_list3=["apple", "kiwi", "mango", "apple", "banana", "tomato", "apple"] 
my_list3.remove(my_list3[5])
my_list3.remove(my_list3[4])
my_list3.remove(my_list3[0])
print(my_list3)
# Nel, correct

#2nd solution
my_list31=["apple", "kiwi", "mango", "apple", "banana", "tomato", "apple"] 
values_for_list = [0, 1, 2, 3, 4, 5, 6] 
dict_2 = {values_for_list[i]: my_list31[i] for i in range(len(values_for_list))}
dict_2.pop(0)
dict_2.pop(4)
dict_2.pop(5)
print(list(dict_2.values()))
# Nel, correct

#3 Write a Python program to get the difference between the two lists.
my_list4=["apple", "kiwi", "mango", "apple", "banana"]
my_list5=["grape", "peach", "apricot", "apple", "banana", "tomato"]
set1=set(my_list4)
set2=set(my_list5)
print(list(set1.difference(set2))) #1st solution
print(list(set1-set2))     #2nd solution
# Nel, correct, but set rempoves duplicate, so you can lose data

#4 Write a Python program to convert a tuple to a dictionary.
tuple_1=("apple", "kiwi", "mango", "apple", "banana")
values=(1, 2, 3, 4, 5)
dict_1={values[i]: tuple_1[i] for i in range(len(values))}
print(dict_1)
# Nel, correct, but you can keep, tuple of other couple tuple and than convert

#5 Write a Python program to add an item in a tuple.
tuple_2=("grape", "peach", "apricot", "apple", "banana", "tomato")
list_1=list(tuple_2)
list_1.append("watermelon")
print(tuple(list_1))
# Nel, correct

#6 Write a Python program to add a key with value to a dictionary.
dict_3={
    "name": "Elya",
    "surname": "Karapetyan",
    "education": "YSU",
    "age": 33,
    "work": "Developer"
    }
dict_3["phone"] = "093942029"
print(dict_3)
# Nel, correct

#7 Write a Python program to get the maximum and minimum value in a dictionary().
dict_4={
    "salary Elya": 1000, 
    "salary Anna": 30000, 
    "salary Anush": 250,
    "salary Syuzi": 5000,
    "salary Ani": 10000
    }
x=dict_4.values()
print(max(x))
print(min(x))
# Nel, correct

#8 Write a Python program to create a union of sets.
set5={"Elya", "Armine", "Levon"}
set6={"Nane", "Shoghik", "Anna", "Elya"}
print(set5 | set6) #1st solution
print(set5.union(set6)) #2nd solution
# Nel, correct

#9 Student  Information
#Write a Python program to create a dictionary with the following information about a student:
# ●	name 
# ●	age 
# ●	address 
# ●	education 
# ●	phone_numbers (store two phone numbers in a list) 
# Then:
# 1.	Print the entire dictionary. 
# 2.	Print only the student's name. 
# 3.	Print only the list of phone numbers. 
# 4.	Add a new key called "email" with your email address. 
# 5.	Print the updated dictionary. ''''''

dict9={
    "name": "Elya",
    "surname": "Karapetyan",
    "address": "Yerevan",
    "education": "YSU",
    "phone numbers": ["093942029", "099942029", "094942029"] 
    }
print(dict9)
print(dict9["name"])
print(dict9["phone numbers"])
dict9["email"]="elelyak@gmail.com"
print(dict9)
# Nel, correct