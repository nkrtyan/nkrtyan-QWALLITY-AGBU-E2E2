f = open("newest.txt", "w+")
f.write("Hello\nit is my first file handling!\n")
f.seek(0)
content = f.read()
print(content)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in alphabet:
    file_name= letter + ".txt"
    open(file_name, "w")
