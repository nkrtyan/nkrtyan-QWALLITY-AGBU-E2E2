f = open("new_file.txt", "a+")
f.write("Hello\nit is my first file handling!\n")
f.seek(0)
print(f.read())


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in alphabet:
    file_name= letter + ".txt"
    open(file_name, "w")
# TODO,do not commit files created by the code _> A-Z
# TODO, start to create the logic inside the function and call them
# TODO, file name give to function as an argument
# Nel, mainly the codebase is correct