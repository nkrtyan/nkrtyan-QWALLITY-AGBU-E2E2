from Library_managment.operations import *

while True:
    print("\n===== Choose one option =====")
    print("1. View all books")
    print("2. Get book information")
    print("3. Add a new book")
    print("4. Delete a book")
    print("5. Exit")
    choice = input("Enter number: ")
    if choice == "1":
        display_books()
    elif choice == "2":
        title = input("Enter book title: ")
        get_book(title)
    elif choice == "3":
        title = input("Title: ")
        author = input("Author: ")
        pages = int(input("Pages: "))
        year = int(input("Publication year: "))
        add_book(title, author, pages, year)
    elif choice == "4":
        title = input("Enter book title: ")
        delete_book(title)
    elif choice == "5":
        print("Շնորհակալություն")
        break
    else:
        print("Invalid choice. Try again.")