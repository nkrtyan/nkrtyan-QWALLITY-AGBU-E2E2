
a = 0
b = 1

print("Ряд Фибоначчи:")
while a <= 50:
    print(a, end=" ")

    a, b = b, a + b

 
    s = "Python 3.13"
letters = 0
digits = 0
for symbol in s:
    if symbol.isalpha():
        letters += 1  
        
    elif symbol.isdigit():
        digits += 1   
        
print ("\nLetters", letters)

print ("Digits", digits)

l = 0
while l <= 6:
    print("\n*")
    l = l + 1
print("*****")
