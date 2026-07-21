# def greeting(name):
#     print ("Hello", name)

# input_name=input("Enter your name\n")
# greeting(input_name)
# greeting("Armen")

# def print_me( name, age):
#     "this is your age and name"
#     print("Name:", name )
#     print("Age:", age)
#     return
# print_me(age=33, name="Elya")

# def display(*name, **address):
#     for items in name:
#         print(items)
#     for items in address.items:
#         print(items)
# display("Elya", "Anna", "Mari", Elya="Yerevan", Anna="NY", Mari="CA")

# def square(x):
#     return x*x
# print(square(4))

# def square(x):
#     print(x*x)
# # print(square(4))

# square(4)


def addition(a, b):
    return a+b
print(addition(20, 25))

book = {
        "Python Crash Course": {
        "author": "Eric Matthes",
        "pages": 544,
        "year": 2022
    },

    "Automate the Boring Stuff with Python": {
        "author": "Al Sweigart",
        "pages": 592,
        "year": 2019
    }
}

from book_data import book

def display_books():
    if not book:
        print("Library is empty") 
    else:
        print(book)

display_books()


# def get_book(title):
#     if title in book.keys():
#         print(book[title])
#     else:
#         print("no book")
# get_book(" Crash Course")


# def add_book(title,author,page,year):
#     book{}


# def delete_book(title)