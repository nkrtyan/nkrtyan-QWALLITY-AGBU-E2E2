numbers = [42, 17, 93, 8, 55, 12, 1]
print("Original list):", numbers)
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(f"Maximum value: {max_val}")

min_val = numbers[0]
for num in numbers:
    if num < min_val:
        min_val = num   
print(f"Minimum value: {min_val}")

total = 0
for num in numbers:
    total += num
print(f"Total value: {total}")

sorted_numbers = numbers.copy()
n = len(sorted_numbers)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if sorted_numbers[j] < sorted_numbers[min_index]:
            min_index = j
    sorted_numbers[i], sorted_numbers[min_index] = sorted_numbers[min_index], sorted_numbers[i]

print("Sorted list:", sorted_numbers)


git commit -m "Add homework 22 solution"
