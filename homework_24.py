"""Write a Python program to get the Fibonacci series between 0 to 50. 
Note : The Fibonacci Sequence is the series of numbers : 
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 0 1 1 2 3 5 8 13 21 34"""

print("\nTask 1")
fib_ser =[]
for i in range(51):
    if i <= 1:
        j = i
    else:
        j = fib_ser[i-1] + fib_ser[i-2]

    if j > 50:
        break
    fib_ser.append(j)

print(*fib_ser)
# Nel, correct, but you can optimize the code

"""Write a Python program that accepts a string and calculates the number of digits and letters.  
Sample Data: Python 3.13
Expected Output:
Letters 6
Digits 3"""

print ("\nTask  2")
letters = []
digits = []

my_string = input("Enter your string: ")

for i in my_string:
    if i.isalpha():
        letters.append(i)
    elif i.isdigit():
        digits.append(i)

print("Letters", len(letters))
print("Digits", len(digits))
# Nel, correct

"""Write a Python program to print alphabet pattern 'L'  
Expected Output:
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*                                                                      
*****"""
print("\nTask 3")
for i in range(8):
    print ("*")
print("*"*6)
# Nel, correct