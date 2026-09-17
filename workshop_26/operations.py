from book_data import books


def display_books():
    print(books)


def get_book(title):
    if title in books:
        info = books[title]
        print(f"Title: {title}")
        print(f"  Author: {info['author']}")
        print(f"  Pages: {info['pages']}")
        print(f"  Year: {info['year']}")
    else:
        print(f"No book called '{title}' was found.")


def add_book(title, author, pages, year):
    if title in books:
        print(f"A book called '{title}' already exists.")
        return

    books[title] = {
        "author": author,
        "pages": pages,
        "year": year,
    }
    print(f"'{title}' was added successfully.")


def delete_book(title):
    if title not in books:
        print(f"No book called '{title}' was found.")
        return

    del books[title]
    print(f"'{title}' was deleted successfully.")