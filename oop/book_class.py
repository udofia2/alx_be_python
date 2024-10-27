class Book:
    """Represents a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Initializes a Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Prints a deletion message."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a human-readable string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns a string that would recreate the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"