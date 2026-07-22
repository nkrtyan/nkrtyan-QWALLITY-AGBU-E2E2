def create_files():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in letters:
        file = open(letter + ".txt", "w")
        file.close()

create_files()