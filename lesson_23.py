#Write a program which will join two tuple and will print reversed joined tuple

tuple_1=(1, 2, 3)
tuple_2=(4, 5, 6)
tuple_3=tuple_1+tuple_2
tuple_4=tuple_2+tuple_1
print("Joined tuple:", tuple_3[::-1])
print("Reversed joined tuple:", tuple_4[::-1])

#ØCreate a list of your favorite fruits. Print the third fruit in the list, add existing fruit to the list, then print list without duplicates.
fruits = ["apple", "banana", "orange", "grape", "kiwi"]
print(fruits[2])
fruits.append("apple")
print(list(set(fruits)))


#third 
my_dict={
    "name": "Elya", 
    "surname": "Karapetyan",
    "education": "YSU"
    }
print(my_dict["education"] )
my_dict["age"]= 33
print(my_dict)