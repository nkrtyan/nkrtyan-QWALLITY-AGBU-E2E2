my_numbers=[7,9,3,11,6]
maximum=7 # TODO, not clear why you give 7 value?
for number in my_numbers:
    if number>maximum:
        maximum=number
print("oroginal list:", my_numbers)
print("Maximum:", maximum)

my_numbers=[7,9,3,11,6]
minimum=7# TODO, not clear why you give 7 value?, instead you should give lits[0]
for number in my_numbers:
    if number<minimum:
        minimum=number
print("oroginal list:", my_numbers)
print("Minimum:", minimum)

my_numbers=[7,9,3,11,6]
result=0
for number in my_numbers:
    result = result + number
print("Sum:", result)
# Nel, mainly the algortithms are written correctly, but not clear why and how you assign value to max and min variables


my_numbers = [7, 9, 3, 11, 6]
result = sorted(my_numbers) # TODO, you need to write implemention, do not use ready function in current homework
print(result)