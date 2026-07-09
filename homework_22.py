# 1. Find the maximum value in a list.
# Get list of numbers from user input
print()
user_input = input("Exercise 1: Find the maximum value\n Enter numbers separated by spaces: ")

# Convert the input string into a list of numbers (floats to allow decimals)
numbers = [float(num) for num in user_input.split()]

 # Print the original list
original_list = numbers
print("Original list:", numbers)

 # Find the maximum value manually
maximum = numbers[0]  # assume the first element is the largest to start

for num in numbers:
    if num > maximum:
        maximum = num

# Print the result
print(f"Exercise 1 result: Maximum value: {maximum}")


# 2. Find the minimum value in a list.

# Get list of numbers from user input
print()
user_input = input("Exercise 2: Find the minimum value\n Enter numbers separated by spaces: ")

# Convert the input string into a list of numbers (floats to allow decimals)
numbers = [int(num) for num in user_input.split()]

# Print the original list
original_list = numbers
print("Original list:", numbers)

# Find the minimum value manually
minimum = numbers[0]  # assume the first element is the smallest to start

for num in numbers:
    if num < minimum:
        minimum = num

# Print the result
print(f"Exercise 2 result: Minimum value: {minimum}")


# 3. Calculate the sum of all elements in a list.

# Get list of numbers from user input
print()
user_input = input("Exercise 3: Calculate the sum\n Enter numbers separated by spaces: ")

# Convert the input string into a list of numbers (floats to allow decimals)
numbers = [float(num) for num in user_input.split()]

# Print the original list
print("Original list:", numbers)

# Calculate the sum manually
total = 0  # start with zero, since we haven't added anything yet

for num in numbers:
    total += num  # same as: total = total + num

# Print the result
print(f"Exercise 3 result: Sum of elements: {total}")


# 4. Sort a list of numbers in ascending order.

# Get list of numbers from user input
print()
user_input = input("Exercise 4: Sort a list in ascending order\n Enter numbers separated by spaces: ")

# Convert the input string into a list of numbers (floats to allow decimals)
numbers = [float(num) for num in user_input.split()]

# Print the original list
original_list = numbers
print("Original list:", numbers)

# Sort the list manually using selection sort
sorted_numbers = numbers.copy()  # work on a copy so the original list stays unchanged

n = len(sorted_numbers)

for i in range(n):
    # assume the current position holds the smallest remaining value
    smallest_index = i

    # look through the rest of the list for something smaller
    for j in range(i + 1, n):
        if sorted_numbers[j] < sorted_numbers[smallest_index]:
            smallest_index = j

    # swap the smallest found value into position i
    sorted_numbers[i], sorted_numbers[smallest_index] = sorted_numbers[smallest_index], sorted_numbers[i]

# Print the result
print(f"Exercise 4 result: Sorted list (ascending): {sorted_numbers}")


# 5. Sort a list of numbers in descending order.

# Get list of numbers from user input
print()
user_input = input("Exercise 5: Sort a list in descending order\n Enter numbers separated by spaces: ")

# Convert the input string into a list of numbers (floats to allow decimals)
numbers = [float(num) for num in user_input.split()]

# Print the original list
original_list = numbers
print("Original list:", numbers)

# Sort the list manually using selection sort
sorted_numbers = numbers.copy()  # work on a copy so the original list stays unchanged

n = len(sorted_numbers)

for i in range(n):
    # assume the current position holds the largest remaining value
    largest_index = i

    # look through the rest of the list for something larger
    for j in range(i + 1, n):
        if sorted_numbers[j] > sorted_numbers[largest_index]:
            largest_index = j

    # swap the largest found value into position i
    sorted_numbers[i], sorted_numbers[largest_index] = sorted_numbers[largest_index], sorted_numbers[i]

# Print the result
print(f"Exercise 5 result: Sorted list (descending): {sorted_numbers}\n")

# TODO, the code is fully correct, but i prefer to review your code :)