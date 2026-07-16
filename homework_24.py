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


3
for i in range(7):
    if i == 6:
        print("*****")
    else:
        print("*")