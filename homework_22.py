my_list = [11, 3, 35, 64, 57, 8, 79]
print(f"{my_list}")

maximum = my_list[0]
for num in my_list:
    if num > maximum:
        maximum = num
print(f"The maximum number in the list is: {maximum}")

minimum = my_list[0]
for num in my_list:
    if num < minimum:
        minimum = num
print(f"The minimum number in the list is: {minimum}")

total_sum = 0
for num in my_list:
    total_sum += num
print(f"The sum of all numbers in the list is: {total_sum}")

sorted_list = my_list[:] 
n = len(sorted_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_list[j] > sorted_list[j + 1]:
            sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
print(f"The sorted list is: {sorted_list}")