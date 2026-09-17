from operations import display_books, get_book, add_book, delete_book


display_books()

get_book("Samvel")

add_book("The Da Vinci Code", "Dan Brown", 489, 2003)
display_books()

get_book("The Da Vinci Code")

delete_book("The Da Vinci Code")
display_books()

get_book("The Metamorphosis")
delete_book("The Metamorphosis")