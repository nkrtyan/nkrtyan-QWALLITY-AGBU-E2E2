#Task 1
with open("myfile.txt", "a+") as file:
    file.write("Hello\n")
    file.write("it's my first file handling!\n")
    file.seek(0)
    lines = file.readlines()

for line in lines: # TODO, this for loop should be inside with open block. 
    print(line.strip())
# TODO, make this logic as an function and call it. Give file name as an argument 

#Task 2
def create_files():
    for i in range(ord('A'), ord('Z') + 1):
        letter = chr(i)
        filename = letter + ".txt"
        open(filename, "w").close()
        print(f"File created: {filename}")

create_files()
# Nel, this function is correct
