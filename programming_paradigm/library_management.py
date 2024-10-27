class Book:
    """Represents a book with title, author, and checkout status."""

    def __init__(self, title, author):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"'{self.title}' has been checked out."
        return f"'{self.title}' is already checked out."

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return f"'{self.title}' has been returned."
        return f"'{self.title}' is already available."


class Library:
    """Manages a collection of books."""

    def __init__(self):
        """Initializes a Library instance."""
        self._books = []

    def add_book(self, book):
        """Adds a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.check_out()
        return f"No book found with title '{title}'."

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f"No book found with title '{title}'."

    def list_available_books(self):
        """Lists all available books."""
        available_books = [f"{book.title} by {book.author}" for book in self._books if not book._is_checked_out]
        if available_books:
            print("\n".join(available_books))
        else:
            print("No available books.")