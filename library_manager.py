from book import Book


def add_book(library):
    """Add a new book to the library. This function does not return anything."""
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    isbn = input("Enter the ISBN: ")

    new_book = Book(title, author, isbn)
    library.append(new_book)

    print("Book added successfully!")


def list_books(library):
    """Display all books in the library. This function does not return anything."""
    if len(library) == 0:
        print("The library is empty")
    else:
        for book in library:
            print(book)


def find_book(library, query):
    """Search the library using a title or author and return the matching book or None."""
    query = query.lower()

    for book in library:
        if query in book.title.lower() or query in book.author.lower():
            return book

    return None


def main():
    """Run the main library management system."""
    my_library = []

    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Find a book")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book(my_library)
        elif choice == "2":
            list_books(my_library)
        elif choice == "3":
            query = input("Enter a book title or author: ")
            book = find_book(my_library, query)

            if book is not None:
                print("Book found:")
                print(book)
            else:
                print("Book not found.")
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose 1-4.")


if __name__ == "__main__":
    main()