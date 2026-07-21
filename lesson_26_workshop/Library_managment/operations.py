from .data import books_data

def display_books():
    if not books_data:
        print("No books available.")
    else:
        print("\nAvailable books:")
        for title, info in books_data.items():
            print(f"\nTitle: {title}")
            print(f"Author: {info['author']}")
            print(f"Pages: {info['pages']}")
            print(f"Year: {info['year']}")

def get_book(title):
    if title in books_data:
        print("\nBook information:")
        print("Title:", title)
        print("Author:", books_data[title]["author"])
        print("Pages:", books_data[title]["pages"])
        print("Year:", books_data[title]["year"])
    else:
        print("Book not found.")

def add_book(title, author, pages, year):
    if title in books_data:
        print("Book already exists.")
    else:
        books_data[title] = {
            "author": author,
            "pages": pages,
            "year": year
        }
        print("Book added successfully.")

def delete_book(title):
    if title in books_data:
        del books_data[title]
        print("Book deleted successfully.")
    else:
        print("Book not found.")