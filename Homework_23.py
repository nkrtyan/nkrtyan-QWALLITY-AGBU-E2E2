my_list = ["1", "2", "3", "5", "1", "5", "7", "2"]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)


my_list = ["a" , "b", "c" , "d" , "e" , "f" , "g"]
del my_list [5]
del my_list [4]
del my_list [0]
print (my_list)


num_list1 = [1, 2, 4, 5, 6, 7]
num_list2 = [1, 2, 3, 4, 5]
difference_list = []
for num in num_list1:
    if num not in num_list2:
        difference_list.append(num)
        print(difference_list)

my_tuple =  (("name","arpine") , ("age", 33) , ("city", "yerevan"))       
my_dict = {} 
for item in my_tuple:
   key = item [0]
   value = item [1]
   my_dict[key] = value
   print(my_dict)

   my_tuple = ("name" , "age" , "city")
   my_tuple = my_tuple + ( "number",)            
   print(my_tuple)

   car_dict = {
       "brand": "BMW", 
       "model": "X6",
       "year": 2020
       }
   x = car_dict.keys()
   y = car_dict.values()
   print(x)
   print (y)


   my_dict = {
    "Math": 8,
    "English": 9,
    "Science": 18,
    "History": 15
}

maximum = max(my_dict.values())
minimum = min(my_dict.values())

print("Maximum value:", maximum)
print("Minimum value:", minimum)



set_1 = {1, 2, 3, 4, 5}
Set_2 = {4, 5, 6, 7, 8}
union_set = set_1.union(Set_2)
print(union_set)



student = {
    "name": "Arpine",
    "age": 33,
    "address": "Yerevan",
    "education": "Cultural Studies",
    "phone_numbers": ["099123456", "093654321"]
}

print(student)
print(student["name"])
print(student["phone_numbers"])

student["email"] = "arpine@example.com"

print(student)