
# Homework 22 

numbers = [44, 39, 11, 7, 75, 69, 104, 9, 55]

print("Original list:", numbers)


# 1. Find the maximum value
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print("Maximum value:", max_value)


# 2. Find the minimum value
min_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num
print("Minimum value:", min_value)


# 3. Calculate the sum of all elements
total = 0
for num in numbers:
    total = total + num
print("Sum of elements:", total)


# 4. Sort the list in ascending order
size = len(numbers)
for i in range(size - 1):
    for j in range(size - 1 - i):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
print("Sorted list:", numbers)