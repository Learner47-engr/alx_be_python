class Book:
    """
    A class to represent a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        _is_checked_out (bool): A private attribute to track the book's availability.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def is_available(self):
        """Checks if the book is available."""
        return not self._is_checked_out

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

class Library:
    """
    A class to manage a collection of books.

    Attributes:
        _books (list): A private list to store Book objects.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book object to the library's collection."""
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added '{book.title}' by {book.author} to the library.")
        else:
            print("Error: The item to add must be a Book object.")

    def check_out_book(self, title):
        """
        Checks out a book from the library by its title.
        
        Args:
            title (str): The title of the book to check out.
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Successfully checked out '{title}'.")
                    return
                else:
                    print(f"Error: '{title}' is already checked out.")
                    return
        print(f"Error: Book '{title}' not found in the library.")

    def return_book(self, title):
        """
        Returns a book to the library by its title.

        Args:
            title (str): The title of the book to return.
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Successfully returned '{title}'.")
                    return
                else:
                    print(f"Error: '{title}' was not checked out.")
                    return
        print(f"Error: Book '{title}' not found in the library.")

    def list_available_books(self):
        """Lists all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"- '{book.title}' by {book.author}")
        else:
            print("No books are currently available.")
