numbers = [ 15, 5, 45, 8, 7, 15, 78, 6]
print(numbers)

max_value = numbers[0]
for element in numbers:
    if element > max_value:
        max_value = element
print("Maximum Value:", max_value)

min_value = numbers[0]
for element in numbers:
    if element < min_value:
        min_value = element
print("Minimum Value:", min_value)

total_sum = 0
for element in numbers:
    total_sum += element
print("Sum of Elements:", total_sum)

sorted_list = list(numbers)
n =  len(sorted_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_list[j] > sorted_list[j + 1]:
            sorted_list[j], sorted_list[j +1] = sorted_list[j+1], sorted_list[j]
print("Sorted_List:", sorted_list)





    