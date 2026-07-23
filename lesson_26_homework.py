f = open("new_file.txt", "a+")
f.write("Hello\nit is my first file handling!\n")
f.seek(0)
print(f.read())


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in alphabet:
    file_name= letter + ".txt"
    open(file_name, "w")
