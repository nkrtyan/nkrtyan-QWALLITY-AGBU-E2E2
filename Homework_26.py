open("text.txt","w") # TODO, extra line
with open("text.txt","r") as file:
    text=file.read()
    print("\nHello")
    print("It's my fist file handling") 
# TODO, need to write , after read it
# TODO, put this functional under function


def create_files():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in letters:
        with open(letter+ ".txt","w") as file:
            pass
        print(letter+".txt")

create_files()
# Nel, this function is correct
