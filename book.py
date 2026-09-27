class Book:
    """Represent a book in the library."""
    def __init__(self, title, author, isbn):
        """Create a book with a title, author, and ISBN."""
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """Return the book information as a readable string."""
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

    def get_details(self):
        """Return the book details as a dictionary."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }