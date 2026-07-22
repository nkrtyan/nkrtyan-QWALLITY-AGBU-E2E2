from library.operations import (
    display_books,
    get_book,
    add_book,
    delete_book
)

display_books()


print("\nAdding new book")
add_book(
    "Harry Potter",
    "J.K Rowling",
    500,
    1997
)


print("\nAll books after adding:")
display_books()


print("\nSearching book:")
get_book("Շունն ու կատուն")


print("\nDeleting book:")
delete_book("Harry Potter")


print("\nFinal list:")
display_books()