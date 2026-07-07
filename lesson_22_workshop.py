'''
Exercises regarding number and string
Write a Python program to calculate the length of a string.
my_string = ‘Here is string for your exercise!’

Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'


Write a Python program to replace ‘cut’ word to ‘dog’
Sample String : 'I have a cut and I love it'
Expected Result : 'I have a dog and I love it'

Write a Python program to reverse 123  to 321 in text.
Sample String : ‘I have 123 books’
Expected Result : 'I have 321 books'

Replace all occurrence of word five to one.
Sample String : "five five was a race horse, two two was one too."
Expected Result "one one was a race horse, two two was one too."


Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

Write a Python program to solve (x + y) * (x + y). 
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49

Write a Python program which converts float values to integer, and sum of two values, then result print with reversed order.
Test Data: x = 2,5 , y = 13.75
Expected Output: 51
'''

my_string = "Here is string for your exercise!"
l = len(my_string)
print(l)

my_string2 = "w3resource"
m = my_string2[:2] + my_string2[-2:]
print(m)

my_string3 = "I have a cat and I love it"
z = my_string3.replace("cat", "dog")
print(z)

my_string4 = "I have 123 books"
words = my_string4.split()
number = words[2]
words[2] = number[::-1]
result = " ".join(words)
print(result)

my_string5 = "five five was a race horse, two two was one too."
result = my_string5.replace("five", "one")
print(result)

numbers = [1, 5, 8, 3]
test_value = 3
print(test_value in numbers)

test_value = -1
print(test_value in numbers)

x = 4 
y = 3
result = (x + y) ** 2
print(result)

x = 2.5 
y = 13.75
sum_values = int(x) + int(y)
reversed_sum = str(sum_values)[::-1]
print(reversed_sum)