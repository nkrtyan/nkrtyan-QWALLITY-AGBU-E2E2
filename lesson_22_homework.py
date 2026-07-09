numbers = [15, 3, 28, 7, 10] 
print (numbers)
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num 
print(maximum)

minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print(minimum)

total = 0
for num in numbers:
    total = total + num
print(total)  

sorted_list = numbers[:]
n = len(sorted_list)
for i in range(n):
    for j in range(0, n - i - 1): # TODO, I hope you understand why you use -i-1
        if sorted_list[j] > sorted_list[j + 1]:
            sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
print("Sorted list:", sorted_list)

# TODO, code with 4 blocks are working correctly



 