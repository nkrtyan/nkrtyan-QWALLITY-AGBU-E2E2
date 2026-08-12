def create_files():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in letters:
        file = open(letter + ".txt", "w")
        file.close()

create_files()
# Nel, working code, just try to use with open block, which will close the file automatically