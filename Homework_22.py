num = [12, 5, 8, 16]

print("Original list:", num)

# Minimum
mini = num[0]
for a in num:
    if a < mini:
        mini = a
print("Minimum value:", mini)

# Maximum
maxi = num[0]
for a in num:
    if a > maxi:
        maxi = a
print("Maximum value:", maxi)

# Sum
total = 0
for a in num:
    total += a
print("Sum of values:", total)

# Sort
for i in range(len(num)):
    for j in range(len(num) - 1):
        if num[j] > num[j + 1]:
            temp = num[j]
            num[j] = num[j + 1]
            num[j + 1] = temp

print("Sorted list:", num)
