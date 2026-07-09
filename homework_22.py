numbers = input("Enter numbers separated by spaces: ").split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print("Original list:", numbers)

# Find maximum
maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number
print("Maximum value:", maximum)

# Find minimum
minimum = numbers[0]
for number in numbers:
    if number < minimum:
        minimum = number
print("Minimum value:", minimum)

# Calculate sum
total = 0
for number in numbers:
    total += number
print("Sum of elements:", total)

# Sort the list 
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
print("Sorted list:", numbers)

# TODO, good job, all four algorithms are working correctly