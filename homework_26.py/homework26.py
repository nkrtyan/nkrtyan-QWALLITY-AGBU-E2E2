file_name = "task1.txt"

with open(file_name, "a+") as file:
    file. write("Hello\n")
    file.write("It's my first handling!\n")

    file.seek(0)
    file_read = file.read()

print(file_read)


import string

def generate_letters_files():
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        with open(file_name, "w") as file:
            file.write("Hello")

generate_letters_files()