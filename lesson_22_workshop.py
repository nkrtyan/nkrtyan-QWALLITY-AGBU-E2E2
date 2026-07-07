#1
my_string1 = "Here is string for your exercise!"
print(len(my_string1))
#2
my_string2 = "w3resource"
result=my_string2[:2]+my_string2[-2:]
print(result)
#3
my_string3= "I have a cat and I love it" 
result=my_string3.replace("cat","dog")
print(result)
#4
text = "I have 123 books"
result = text.replace("123", "321")
print(result)
#5
text = "five five was a race horse, two two was one too."
result = text.replace("five", "one")
print(result)
#6
data1=[1, 5, 8, 3]
data2=[1, 5, 8, 3]
print(3 in data1)
print(-1 in data2)

#7
x=4
y=3
print((x + y)**2)

#8
a=2.5
b=13.75
c=int(a)+int(b)

print(''.join(reversed(str(c))))
