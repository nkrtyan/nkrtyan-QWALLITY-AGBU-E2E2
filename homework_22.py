'''Lesson_22: Homework->Implement List Operations
Create one Python program that implements the following list operations:

Find the maximum value in a list.
Find the minimum value in a list.
Calculate the sum of all elements in a list.
Sort the list in ascending order.


Requirements

Use any list of numbers as input.
Do not use Python's built-in max(), min(), sum(), sort(), or sorted() functions.
Implement the logic yourself using the Python concepts you have learned so far.
Print the original list and the result of each operation in the terminal.


Submission

Save your solution in one homework_22.py file.
Commit and push your code to your Git repository.
Create a Pull Request.'''

my_list = [5, 2, 9, 1, 5, 6]
print(my_list)

#Find the maximum value in a list.
maximum = my_list[0]
for item in my_list:
    if item > maximum:
        maximum = item
print("Maximum value:", maximum)

#Find the minimum value in a list.
minimum = my_list[0]
for item in my_list:
    if item < minimum:
        minimum = item
print("Minimum value:", minimum)

#Calculate the sum of all elements in a list.
summary = 0
for item in my_list:
    summary += item
print("Sum of all elements:", summary)

#Sort the list in ascending order. Couldn't use built-in sort() or sorted() functions
