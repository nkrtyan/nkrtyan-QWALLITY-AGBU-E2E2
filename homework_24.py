#1. 
#  Write a Python program to get the Fibonacci series between 0 to 50. 
# Note : The Fibonacci Sequence is the series of numbers : 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 0 1 1 2 3 5 8 13 21 34

print()
# 1.1
first_number = 0
second_number = 1

while first_number <= 50:
    print(f"{first_number}", end=" ")
    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number

# 1.2
fib_numbers = [0, 1] 

while fib_numbers[-1] <= 50:
    next_number = fib_numbers[-2] + fib_numbers[-1]
    fib_numbers.append(next_number)
fib_numbers.pop()
print(f"{fib_numbers}")

# Nel, both versions are correct

# 2. Write a Python program that accepts a string and calculates the number of digits and letters.  
# Sample Data: Python 3.13
# Expected Output:
# Letters 6
# Digits 3

print()
# 2.1
my_string = "Python 3.13"
letters_count = 0
digits_count = 0

for char in my_string:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1

print(f"Letters: {letters_count}")
print(f"Digits: {digits_count}")
# Nel, correct

# 2.2
# text = input("Enter a string: ")
text = "Python 3.13"

letters_count = 0
digits_count = 0

for char in text:
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'): 
        letters_count += 1
    elif char >= '0' and char <= '9':
        digits_count += 1

print(f"Letters: {letters_count}")
print(f"Digits: {digits_count}")
# Nel, correct, but i prefer the firts version

# 2. Write a Python program to print alphabet pattern 'L'  
# Expected Output:
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *                                                                      
# *****
print()
# 3.1
line_count = 7
for i in range(line_count):
    if i < line_count - 1:
        print("*")
    else:
        print("*" * 5)

# 3.2
line_count = [1, 2, 3, 4, 5, 6, 7]
for i in line_count[:6]:
    if line_count[i] != 6:
        print("*")
    else:
        print("*" * 5)
#Nel, both versions are correct