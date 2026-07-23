f = open("my_text.txt", "a+") #1
my_list = ["Hello\n", "it's my first handling!\n"]
for i in my_list:
    f.write(i)
f.seek(0)
print(f.read())
f.close()

# TODO, make this logic as a function and call it, pass file name as an argument to the function
# TODO, the second task is absent
# TODO, do not commit files created by the code