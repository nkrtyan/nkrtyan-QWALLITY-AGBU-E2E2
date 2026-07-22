f = open("my_text.txt", "a+") #1
my_list = ["Hello\n", "it's my first handling!\n"]
for i in my_list:
    f.write(i)

f.seek(0)
print(f.read())
f.close()