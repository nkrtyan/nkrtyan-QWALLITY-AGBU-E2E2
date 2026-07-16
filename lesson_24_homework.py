#Write a Python program to get the Fibonacci series between 0 to 50
sum = 0
first_num = 0
second_num = 1
print(first_num)
while sum <=50:
    print(second_num)
    sum = first_num + second_num
    first_num = second_num
    second_num = sum
print()
# TODO, you should primt numbers next to each other

#Write a Python program that accepts a string and calculates the number of digits and letters. 
my_text = "Python 3.13"
char_count = 0
int_count = 0
for char in "Python 3.13":
    if char.isalpha():
        char_count +=1
    elif char.isdigit():
        int_count +=1

print(f"Digits count is: {int_count}")
print(f"letters count is: {char_count}", "\n")
# Nel, correct

#Write a Python program to print alphabet pattern 'L'
i = 0
while i<5:
    print("*")
    i+=1

for item in range(5): # TODO, no need additional cycle, optimise code
    print("*", end=" ")

