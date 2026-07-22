import string

def generate_files():
    alphabet_str = string.ascii_uppercase

    for i in alphabet_str:
        with open(f"lesson_26_homework/task2/{i}.txt", "a"):
            pass
generate_files()