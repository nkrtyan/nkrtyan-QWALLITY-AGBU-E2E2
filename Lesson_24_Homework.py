"""1.	Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34

2.	Write a Python program that accepts a string and calculates the number of digits and letters.  
Sample Data: Python 3.13
Expected Output:
Letters 6
Digits 3

3.	Write a Python program to print alphabet pattern 'L'  
Expected Output:
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*****
"""

a = 0
b = 1

while a <= 50:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
# Nel, correct

my_text = "Python 3.13"
letters = 0
digits = 0
for char in my_text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters", letters)
print("Digits", digits)
# Nel, correct

for i in range(6): #3
    print("*")
print("*****") # TODO, just print 5* "*"


for i in range(7): #3 
    if i == 6:
        print("*****")
    else:
        print("*")
# Nel correct