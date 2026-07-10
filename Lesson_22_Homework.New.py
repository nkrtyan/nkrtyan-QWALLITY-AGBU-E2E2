"""Create one Python program that implements the following list operations:

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
Create a Pull Request."""

numbers = [9, 11, 2, 1, 7, 3, 5, 8] #Find the maximum value in a list.
maximum = numbers[0]
for value in numbers[1:]:
    if value > maximum:
        maximum = value
print("Maximum value:", maximum)


minimum = numbers[0] #Find the minimum value in a list.
for value in numbers[1:]:
    if value < minimum:
        minimum = value
print("Minimum value:", minimum)

total = 0 #Calculate the sum of all elements in a list.
for value in numbers:
    total += value
print("Sum of all elements:", total)


sorted_numbers = numbers[:] #Sort the list in ascending order.
for i in range(len(sorted_numbers)):
    min_index = i
    for j in range(i + 1, len(sorted_numbers)):
        if sorted_numbers[j] < sorted_numbers[min_index]:
            min_index = j
    if min_index != i:
        sorted_numbers[i], sorted_numbers[min_index] = sorted_numbers[min_index], sorted_numbers[i]
print("Sorted list (ascending):", sorted_numbers)
