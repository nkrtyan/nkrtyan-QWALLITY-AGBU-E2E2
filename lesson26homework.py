f=open("my_text.txt","+w")
f.write("hello\ni'ts my first file handling!")
f.seek(0)
my_data = f.read()
print(my_data)
f.close()
# TODO, keep both tasks inside the same file
# TODO, make this functionality as an function and call it. Give file name as an argument
# Nel, code is correct