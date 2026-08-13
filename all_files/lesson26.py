# f=open("test.file.txt", "r")
# data=f.readline().strip()
# print(data)


# f.close()

# # Opening the file manually
# file = open("test.file.txt", "w+")
# file.write("Hello\nWorld\nElya\nAram")
# file.seek(0)
# # Using readline() to read lines one by one
# print(file.readline().strip())  # Reads first line
# print(file.readline().strip())  # Reads second line
# print(file.readline().strip())
# print(file.readline().strip())

# file.close()

# Create a list of lines to write (without \n)
# lines_to_write = ["Line 1", "Line 2", "Line 3"]

# # Open the file in write mode and use writelines, adding newlines automatically
# f = open("test.txt", 'wt', encoding='utf-8')
# f.writelines(line + '\n' for line in lines_to_write)
# f.seek(0)

# # Reopen the file in read mode to read its contents
# f = open("test.txt", 'rt', encoding='utf-8')
# data = f.read()
# print(data)
# f.close()

# f=open("test.file.txt", "a+")
# data=f.write("\nElya1")
# f.seek(0)
# print(data)


# f=open("test.file.txt", "a+")
# f1=open("test.file.txt", "r")

# def testing(added_text):
#     added_text=f.write("\nHello\nit’s my first file handling!")
#     print(added_text)
#     f.close()
#     changed_file=f1.read()
#     print(changed_file)
# testing(added_text="123")


