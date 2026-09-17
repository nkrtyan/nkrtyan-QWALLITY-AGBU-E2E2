# 1 Write a Python program which will open file, if not exist than create it.  Append the following text with two lines: 
# Hello –> first line
# it’s my first file handling! –> second line
# Read data from the file and print in the Terminal. 

def creating_file(new_file):
    with open("new_file", "a") as f:
        f.write ("Hello\nIts my fist handling!")
        f.seek(0)

    with open("new_file", "r") as f:
        text = f.read()
        print(text)
creating_file("homework_26")


# 2. Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
def create_file2():
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        file = open(letter + ".txt", "w")
        file.close()


create_file2()
    
