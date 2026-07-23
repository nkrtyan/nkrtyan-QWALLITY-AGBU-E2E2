"""
Write a Python program which will open file, if not exist than create it.  Append the following text with two lines: 
Hello –> first line
it’s my first file handling! –> second line
Read data from the file and print in the Terminal. 

Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.
"""
f = open("test_file","a")
f.write("Hello\n")
f.write("It's my first file handling!\n")
f.close()
