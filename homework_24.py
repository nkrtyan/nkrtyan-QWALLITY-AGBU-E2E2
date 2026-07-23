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