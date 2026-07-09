# 1
# Exercises regarding number and string
# Write a Python program to calculate the length of a string.
# my_string = ‘Here is string for your exercise!’

print()
my_string = "Here is string for your exercise!"
print(f"Exercise 1: {len(my_string)}")

# 2
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'

print()
string1 = "w3resource"
string2 = string1[0:2] + string1[-2:]
print(f"Exercise 2: {string2}")

# 3
# Write a Python program to replace ‘cut’ word to ‘dog’
# Sample String : 'I have a cut and I love it'
# Expected Result : 'I have a dog and I love it'

print()
string1 = "I have a cut and I love it."
string2 = string1.replace("cut", "dog")
print(f"Exercise 3: {string2}")

# 4
# Write a Python program to reverse 123  to 321 in text.
# Sample String : ‘I have 123 books’
# Expected Result : 'I have 321 books'

print()
string1 = "I have 123 books"
string2 = string1.replace("123", "321")
print(f"Exercise 4: {string2}")  

# 5
# Replace all occurrence of word five to one.
# Sample String : "five five was a race horse, two two was one too."
# Expected Result "one one was a race horse, two two was one too."

print()
string1 = "five five was a race horse, two two was one too."
string2 = string1.replace("five", "one")
print(f"Exercise 5: {string2}")

# 6
# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

print()
list1 = [1, 5, 8, 3]
test_data = input("Exercise 6: Enter a number to check if it is in the list: ")
if test_data in list1:
    print(f"Exercise 6: {test_data} -> {list1} : True")
else:
    print(f"Exercise 6: {test_data} -> {list1} : False")

# 7
# Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

print()
x = 4
y = 3
result = (x + y) ** 2
print(f"Exercise 7: ({x} + {y}) ^ 2 = {result}")

# 8
# Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
# Test Data: x = 2,5 , y = 13.75
# Expected Output: 51

print()
x = 2.5
y = 13.75
sum_result = int(x) + int(y)
reversed_result = str(sum_result)[::-1]
print(f"Exercise 8: Sum of {int(x)} and {int(y)} is {sum_result}, and its reversed order is {reversed_result}\n")
