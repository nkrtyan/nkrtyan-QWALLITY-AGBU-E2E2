f = open("my_text.txt", "a+")
my_list = ["Hello\n", "it's my first handling!"]
for i in my_list:
    f.writelines(i)

f.seek(0)
my_data = f.read()
print(my_data)
f.close()