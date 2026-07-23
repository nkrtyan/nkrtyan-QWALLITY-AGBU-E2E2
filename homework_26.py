# 1. Write a Python program which will open file, if not exist than create it.  Append the following text with two lines: 
# Hello –> first line
# it’s my first file handling! –> second line
# Read data from the file and print in the Terminal. 


f=open("test.file.txt", "a+")
added_text=f.write("\nHello\nit’s my first file handling!")
print(added_text)
f.close()
f1=open("test.file.txt", "r")
changed_file=f1.read()
print(changed_file)
# TODO, code is correct, but put the logic inside function and give filename as an argument

# 2. Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
# TODO, finish when have time


