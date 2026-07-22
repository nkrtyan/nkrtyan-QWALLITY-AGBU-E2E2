from .data import books

def display_books():
    if len(books) == 0:
        print("No books available")
    else:
        for title, info in books.items():
            print("----------------")
            print("Title:", title)
            print("Author:", info["author"])
            print("Pages:", info["pages"])
            print("Year:", info["year"])



def get_book(title):
    if title in books:
        print(books[title])
    else:
        print("Book not found")



def add_book(title, author, page, year):

    if title in books:
        print("Book already exists")

    else:
        books[title] = {
            "author": author,
            "pages": page,
            "year": year
        }

        print("Book added successfully")



def delete_book(title):

    if title in books:
        del books[title]
        print("Book deleted")

    else:
        print("Book not found")