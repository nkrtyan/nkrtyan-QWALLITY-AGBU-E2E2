my_string ="Here is string for your exercises!"
print(len(my_string))
my_string = "w3resource"
result = my_string[: 2] + my_string[-2: ]
print(result)

my_string = "I have a cat and I love it"
result =my_string.replace("cat", "dog")
print(result)

my_string = "I have 123 books"
my_list = my_string.split()
print(my_list[2])
a = (my_list[2])
print(''.join(reversed(a)))

my_string = "five five was a race horse, two two was one too."
result = my_string.replace("five", "two")
print(result)

numbers =[1, 5, 8, 3]
print(3 in numbers)
print(-1 in numbers)

x = 4
y = 3
result = (x+y) * (x+y)
print(result)

x = 2.5
y = 13.75
total = int(x) +int(y)
result =str(total)[::-1]
print(result)
