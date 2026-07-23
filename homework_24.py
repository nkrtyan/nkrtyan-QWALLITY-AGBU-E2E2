<<<<<<< HEAD
1.1
x, y = 0, 1
while x <= 50:
    print (x, end = " ")
    x, y = y, x+y

1.2
x, y = 0, 1
while x<+ 50:
    print (x, end = " ")
    temp = x
    x = y
    y = temp + y
# nel, both versions are correct

2
text = "I have been learning QA for 2 months"
letters = 0
digits = 0
all_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
all_digits = "0123456789"
for char in text:
    if char in all_letters:
        letters += 1
    elif char in all_digits:
        digits += 1
print("Letters", letters)
print("Digits", digits)
# TODO, correct but there are alsi isalpha() and isdigit() functions

3
for i in range(7):
    if i == 6:
        print("*****") # TODO, use 6*"*"
    else:
        print("*")
# Nel, correct
=======
a, b = 0, 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a + b

text="Python 3.13"
letters=0
digits=0
for i in range(len(text)):
    char = text[i]
    if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letters += 1
    elif char in "0123456789":
        digits += 1
print("Letters", letters)
print("Digits", digits)

for i in range(7):
    if i == 6:
        print("*****")
    else:
        print("*")
>>>>>>> c24c497416a2603309f447eb9f40b7d590e2c99e
