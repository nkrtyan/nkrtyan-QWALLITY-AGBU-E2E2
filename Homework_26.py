open("text.txt","w")
with open("text.txt","r") as file:
    text=file.read()
    print("\nHello")
    print("It's my fist file handling")

def create_files():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in letters:
        with open(letter+ ".txt","w") as file:
            pass
        print(letter+".txt")

create_files()

