rom .data import books


def display_books():
    if not books:
        print("No books available.")
    else:
        print("\nAvailable books:")
        for title, info in books.items():
            print(f"\nTitle: {title}")
            print(f"Author: {info['author']}")
            print(f"Pages: {info['pages']}")
            print(f"Year: {info['year']}")


def get_book(title):
    if title in books:
        print("\nBook information:")
        print("Title:", title)
        print("Author:", books[title]["author"])
        print("Pages:", books[title]["pages"])
        print("Year:", books[title]["year"])
    else:
        print("Book not found.")


def add_book(title, author, pages, year):
    if title in books:
        print("Book already exists.")
    else:
        books[title] = {
            "author": author,
            "pages": pages,
            "year": year
        }
        print("Book added successfully.")


def delete_book(title):
    if title in books:
        del books[title]
        print("Book deleted successfully.")
    else:
        print("Book not found.")