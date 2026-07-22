from .data import books

def display_books():

    if books == {}:
        print("Գրքեր չկան")

    else:
        for book_name in books:
            print("----------------")
            print("Անուն:", book_name)
            print("Հեղինակ:", books[book_name]["author"])
            print("Էջեր:", books[book_name]["pages"])
            print("Տարի:", books[book_name]["year"])



def get_book(title):

    if title in books:
        print("Գիրքը գտնվեց")
        print("Հեղինակ:", books[title]["author"])
        print("Էջեր:", books[title]["pages"])
        print("Տարի:", books[title]["year"])

    else:
        print("Գիրքը չկա")



def add_book(title, author, page, year):

    if title in books:
        print("Այս գիրքն արդեն կա")

    else:
        books[title] = {
            "author": author,
            "pages": page,
            "year": year
        }

        print("Գիրքը ավելացվեց")



def delete_book(title):

    if title in books:
        del books[title]
        print("Գիրքը ջնջվեց")

    else:
        print("Գիրքը չկա")