class Book:
    """Base class representing a book."""

    def __init__(self, title, author):
        """Initializes a Book instance."""
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a string representation of the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initializes an EBook instance."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Returns a string representation of the eBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a print book."""

    def __init__(self, title, author, page_count):
        """Initializes a PrintBook instance."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Returns a string representation of the print book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library with a collection of books."""

    def __init__(self):
        """Initializes a Library instance."""
        self.books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)