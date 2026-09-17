def generate_text_files():  
    for i in range(ord("A"), ord("Z")+1): # TODO, good search, but try to understand , you can just use range(65, 91) instead
        letter = chr(i)
        filename = f"{letter}.txt"
        f = open(filename, "w")
        f.close()
    print("26 files")
generate_text_files()
# Nel, correct