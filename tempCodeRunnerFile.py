with open("new.txt","w+") as f:
    f.write("Hello\nit’s my first file handling!")
    f.seek(0)
    data=f.read()
    print(data)