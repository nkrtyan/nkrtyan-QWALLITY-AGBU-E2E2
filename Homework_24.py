max = 50
for i in range(max):
    if i > 1:
        i = fib1 + fib2
        fib1 = fib2
        fib2 = i
    else:
        i = i
        fib1 = 0
        fib2 = 1
    if i < max:
        print(i, end = " ")
print()
# Nel, correct

my_text = "Python 3.13"
letters = 0
digits = 0

for char in my_text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)
# Nel, correct

height = 7
for i in range(height - 1):
    print("*")
print("*****") # TODO, 6*"*"
#Nel, correct

