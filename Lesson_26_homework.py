# Write a Python program which will open file, if not exist than create it.  Append the following text with two lines: 

f=open("new.txt","w+")
f.write("Hello\nit’s my first file handling!")
f.seek(0)
data=f.read()
print(data)
f.close()

# Using the with open statement
with open("new.txt","w+") as f:
    f.write("Hello\nit’s my first file handling!")
    f.seek(0)
    data=f.read()
    print(data)
# TODO, but the logic inside the function and call it, give file name as an argument


# Write a Python function which generates 26 text files named A.txt, B.txt, and so on up to Z.txt.

for i in range(26):
    letter = chr(65 + i)
    f = open(f"{letter}.txt", "w")
    f.close()
# TODO, the same here, make this logic as an function


#  Delete the 26 created files
# import os
# for i in range(26):
#     letter = chr(65 + i)
#     os.remove(f"{letter}.txt")
# TODO, no need to remove after creation directly, you should finish full files creation, after ask from terminal and delete when user confirms.We will talk during lesson