with open('lesson_26_homework/task1/test.txt', 'a+') as file:
    my_list = ["Hello\n", "It's my first file handling!"]

    for i in my_list:
        file.writelines(i)

    file.seek(0)
    file_read = file.read()

print(file_read)
# TODO, no need to commit test.txt file
# TODO, put this functional inside function and call it