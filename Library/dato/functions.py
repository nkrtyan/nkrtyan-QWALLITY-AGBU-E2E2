from dato import data

data.book

def display_books():
    if not data.book:
        print("Library is empty") 
    else:
        print(data.book)

display_books()



def get_book(title):
    if title in data.book.keys():
        print(data.book[title])
    else:
        print(f"no {title}")
get_book("Python Crash Course")


def add_book(title,author,page,year):
    if title not in data.book.keys():
       data.book[title] = {
           "author": "Mark Lutz",
           "pages": 1600,
           "year": 2013
        }
       print(f"{title} was added")
    else:
        print(f"{title} exists")
add_book("Learning Python (5th Edition)", "Mark Lutz", 1600, 2013)
print(data.book)


def delete_book(title):
    if title in data.book.keys():
        del data.book[title]
        print(f"{title} was removed")
    else:
        print(f"{title} doesn't exist")
delete_book("Learning Python (5th Edition)")