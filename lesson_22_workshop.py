# Exercises regarding number and string
# Write a Python program to calculate the length of a string.
# my_string = ‘Here is string for your exercise!’
my_string = 'Here is string for your exercise!'
print(len(my_string))



# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
string = "w3resource"
var1 = string[0:2]
var2 = string[-2:]
new_string = var1 + var2
print(new_string)

# Write a Python program to replace ‘cut’ word to ‘dog’
# Sample String : 'I have a cat and I love it'
# Expected Result : 'I have a dog and I love it'
old_string = "I have a cat and I love it"
newstring = old_string.replace("cat", "dog")
print(newstring)

# Write a Python program to reverse 123  to 321 in text.
# Sample String : ‘I have 123 books’
# Expected Result : 'I have 321 books'
text = "I have 123 books"
words = text.split()
print(words)
number = words[2]
words[2] = number[::-1]
result = " ".join(words)
print(result)

# Replace all occurrence of word five to one.
# Sample String : "five five was a race horse, two two was one too."
# Expected Result "one one was a race horse, two two was one too."
my_text = "five five was a race horse, two two was one too."
new_text = my_text.replace("five", "one")
print(new_text)

# Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
numbers = [1, 5, 8, 3]
print(3 in numbers)
print(-1 in numbers)

# Write a Python program to solve (x + y) * (x + y). 
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49
x = 4
y = 3
result = (x + y) * (x + y)
print(f"( {x} + {y}) ^ 2 = {result}")

# Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
# Test Data: x = 2,5 , y = 13.75
# Expected Output: 51
x = 2.5
y = 13.75
x = int(x)
y = int(y)
result = x + y
result = str(result)
result = result[::-1]
result = int(result)
print(result)