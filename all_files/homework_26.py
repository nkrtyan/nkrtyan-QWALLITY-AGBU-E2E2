# 1. Write a Python program which will open file, if not exist than create it.  Append the following text with two lines: 
# Hello –> first line
# it’s my first file handling! –> second line
# Read data from the file and print in the Terminal. 


<<<<<<< HEAD
def create_file(filename):
    with open(filename, "a+") as f:
        added_text=f.write("Hello\nit’s my first file handling!")
        print(added_text)

    with open(filename, "r") as f1:
        changed_file=f1.read()
        print(changed_file)

create_file("test.file.txt")

=======
f=open("test.file.txt", "a+")
added_text=f.write("\nHello\nit’s my first file handling!")
print(added_text)
f.close()
f1=open("test.file.txt", "r")
changed_file=f1.read()
print(changed_file)
>>>>>>> 2e4169d5a89bb85cc9d9b7af15ce98eaba3e820d
# TODO, code is correct, but put the logic inside function and give filename as an argument

# 2. Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
# TODO, finish when have time

# TODO, finish when have time

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for item in alphabet:
    with open(item + ".txt", "w") as file:
        pass
    print(item+".txt")
    