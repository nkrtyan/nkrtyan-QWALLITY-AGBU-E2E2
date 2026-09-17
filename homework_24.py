# #Write a Python program to print alphabet pattern 'L' 
# for item in range(1,7):
#     print ("*")
# if item == 6:
#         print("*" * 5)
# else:
#         print("*")
# Nel, correct

# #Write a Python program to get the Fibonacci series between 0 to 50. 
# a=0
# b=1
# while a<50:
#        print(a)
#        temp=a
#        a=b
#        b=temp+b
# TODO, the numbers should be printed next to each other

# # Write a Python program that accepts a string and calculates the number of digits and letters.  
# # Sample Data: Python 3.13

text = "Python 3.13"
letters = 0
number = 0
for char in text:
    if char.isalpha():
        letters = letters + 1
    elif char.isdigit():
        number = number + 1
print("Letters", letters)
print("Number", number)
# Nel, correct
