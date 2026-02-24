from .utils import track_access, permission_check

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    def __str__(self):
        # User-friendly string representation
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        # Return number of pages
        return self.pages

    def __eq__(self, other):
        # Check equality based on title and author
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

class Library:
    def __init__(self):
        self._books = []

    def __len__(self):
        return len(self._books)

    def __getitem__(self, position):
        # Makes the library iterable
        return self._books[position]

    @permission_check("Admin")
    def add_book(self, user, book):
        """
        Adds a book to the library. Requires Admin role.
        """
        self._books.append(book)
        print(f" Book added: {book}")

    @track_access
    def borrow_book(self, book_title):
        """
        Borrows a book by title. Logs access.
        """
        for book in self._books:
            if book.title == book_title and not book.is_borrowed:
                book.is_borrowed = True
                print(f" You have borrowed: {book.title}")
                return
        print(f" Book '{book_title}' not available.")

    @track_access
    def return_book(self, book_title):
        for book in self._books:
            if book.title == book_title and book.is_borrowed:
                book.is_borrowed = False
                print(f" Returned: {book.title}")
                return
        print("Could not process return.")