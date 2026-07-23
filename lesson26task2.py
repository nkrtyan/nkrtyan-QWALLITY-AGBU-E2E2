def generate_text_files():
    for i in range(ord("A"), ord("Z")+1):
        letter = chr(i)
        filename = f"{letter}.txt"

        f = open(filename, "w")
        f.close()
    print("26 files")
generate_text_files()