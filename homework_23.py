#1 Write a Python program to remove duplicates from a list(write logic of the set, do not use set)
numbers = [5, 2, 5, 8, 2, 1, 8]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
# Nel, correct


#2 Write a Python program which print a specified list after removing the 0th, 4th and 5th elements.  
my_list = [14, 40, 37, 7, 5, 6, 3]
new_list = []
for item in range(len(my_list)):
    if item != 0 and item != 4 and item != 5:# TODO, you can write item in [0,4,5]
        new_list.append(my_list[item])
print(new_list)
# Nel, correct


#3 Write a Python program to get the difference between the two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
dif = []
for item in list1:
    if item not in list2:
        dif.append(item)
print(dif)
# Nel, correct


#4 Write a Python program to convert a tuple to a dictionary.
studentstuple=("Gayane",27), ("Alen", 28), ("Aram", 29)
studentsdic = {}
for item in studentstuple:
    studentsdic[item[0]] = item [1]
print(studentsdic)
# Nel, correct

#5 Write a Python program to add an item in a tuple.
#firstsolution
cars = ("Mercedes", "Kia", "BMW", "Toyota")
new_car = ("BYD")
cars = cars + (new_car,)
print(cars)

#secondsolution
cars = ("Mercedes", "Kia", "BMW", "Toyota")
temp=list(cars)
temp.append ("BYD")
cars=tuple(temp)
print(cars)
# Nel, correct


#6 Write a Python program to add a key with value to a dictionary.

book={
    "book_name": "Harry Potter",
    "years": 1997,
    "author" : "J.K.Rowling"
}
print(book["author"])
book["parts"] = 7
print(book)
# Nel, correct


#7 Write a Python program to get the maximum and minimum value in a dictionary().

#first
fam={
   "Gayane": 1998,
   "Anahit":2000,
   "Albert":2005
}
values=list(fam.values())
maximum = values[0]
minimum = values [0]
for number in values:
    if number>maximum:
        maximum=number
    if number<minimum:
        minimum=number
print(maximum)
print(minimum)

#second
fam={
   "Gayane": 1998,
   "Anahit":2000,
   "Albert":2005
}
print(max(fam.values()))
print(min(fam.values()))
# Nel, correct


#8 Write a Python program to create a union of sets.
#first
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)

#senond 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 | set2
print(set3)
# Nel, correct

#9 Student  Information
student = {
    "name": "Gayane",
    "age": 27,
    "address": "Hrazdan",
    "education": "YSU",
    "phone_numbers": ["+37494441207", "+37477100866"]
}

print(student)
print(student["name"])
print(student["phone_numbers"])

student["email"] = "gayane.khachatran@gmail.com"
print(student)
# Nel, correct, good for you
