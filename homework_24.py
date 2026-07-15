# 1. Write a Python program to get the Fibonacci series between 0 to 50.
a = 0
b = 1

while True:
    if a > 50:
        break

    print(a, end=" ")

    c = a + b
    a = b
    b = c


    #2. Write a Python program that accepts a string and calculates the number of digits and letters. Sample Data: Python 3.13
    text = "Python 3.13"
    letters = 0
    digits = 0

for i in text:
    if i.isalpha():
        letters += 1
        continue

    if i.isdigit():
        digits += 1
        continue

print("Letters", letters)
print("Digits", digits)

#Write a Python program to print alphabet pattern 'L'
i = 0

while i < 7:
    if i == 6:
        print("*****")
        break
    else:
        print("*")
        i += 1