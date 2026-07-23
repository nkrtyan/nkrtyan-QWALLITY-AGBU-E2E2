# 1 Write a Python program which will open file, if not exist than create it.  Append the following text with two lines: 
# Hello –> first line
# it’s my first file handling! –> second line
# Read data from the file and print in the Terminal. 

file = open("homework.txt", "a")

file.write("Hello\n")
file.write("it’s my first file handling!\n")

file.close()


file = open("homework.txt", "r")

data = file.read()

print(data)

file.close()



# Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.


import string

def creatingfiles():
    for letter in string.ascii_uppercase:
        file = open(f"{letter}.txt", "w")
        file.close()


creatingfiles()