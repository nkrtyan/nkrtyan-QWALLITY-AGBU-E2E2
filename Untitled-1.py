file_name = "task1.txt"
with open(file_name, "a+") as file:
    file.write = ("Hello\n")
    file.write = ("It's my first file handling!\n")

    file.seek(0)
    file_read = file.read()

print(file_read)




import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"

    with open(filename, "w") as file:
        file.write("Hello")
