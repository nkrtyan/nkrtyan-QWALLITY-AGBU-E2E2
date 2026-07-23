# 1. Write a Python program which will open file, if not exist than create it.  Append the following text with two lines: 
# Hello –> first line
# it’s my first file handling! –> second line
# Read data from the file and print in the Terminal. 


def create_file(filename):
    with open(filename, "a+") as f:
        added_text=f.write("Hello\nit’s my first file handling!")
        print(added_text)

    with open(filename, "r") as f1:
        changed_file=f1.read()
        print(changed_file)

create_file("test.file.txt")

# TODO, code is correct, but put the logic inside function and give filename as an argument

# 2. Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.

# TODO, finish when have time

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for item in alphabet:
    with open(item + ".txt", "w") as file:
        pass
    print(item+".txt")
    