"""
Library Book Management System
Author: Stavion Colquitt
Date:   2026-10-02
Tier:   Base Level
Description:
    Models library books as objects using a Book class. Each Book stores
    its own data and handles its own checkout, return, and status
    reporting. The main program manages a collection of Book objects.

TEST RESULTS (verified by running the program)

    [x] A newly created Book prints with all five fields plus "Available"
        Actual output line:
978-0441013593    Dune                        Frank Herbert           1965   Science Fiction     Available
            __str__ returns a string rather than printing one, and the
            status portion comes from get_status().

    [x] check_out() on an available book
            Returned True. available changed True -> False and borrower
            was set to the patron name.
            Output: 'The Great Gatsby' checked out to Jordan.

    [x] check_out() on a book already checked out
            Returned False. available stayed False and borrower stayed
            "Jordan" - no attribute was modified.
            Output: 'The Great Gatsby' is already checked out.

    [x] return_book() on a checked-out book
            Returned the confirmation string, reset available to True
            and borrower to None.
            Output: 'Educated' has been returned and is now available.

    [x] Sorted display
            Beloved, Dune, Educated, The Great Gatsby, The Nickel Boys,
            Thinking in Systems - alphabetical by title. sorted() builds
            a new list, so the original collection order is unchanged.

    [x] Available filter
            After the checkouts and the return, The Great Gatsby is the
            only title missing from the filtered list. Built with a list
            comprehension, not a manual append loop.

    [x] Column alignment
            Checked against "Historical Fiction" (18 characters), the
            longest genre in the collection - columns still separate
            cleanly at a field width of 20.
"""


class Book:
    """A single library book that manages its own checkout state."""

    def __init__(self, title, author, isbn, year, genre):
        """Store the book's details and set it as available."""
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self.available = True
        self.borrower = None

    def __str__(self):
        """Return a formatted one-line summary of this book."""
        return (f"{self.isbn:<18}{self.title:<28}{self.author:<24}"
                f"{self.year:<7}{self.genre:<20}{self.get_status()}")

    def check_out(self, patron_name):
        """Check the book out if available. Returns True on success."""
        if self.available:
            self.available = False
            self.borrower = patron_name
            return True
        return False

    def return_book(self):
        """Reset availability and return a confirmation string."""
        self.available = True
        self.borrower = None
        return f"'{self.title}' has been returned and is now available."

    def get_status(self):
        """Return a short string describing availability."""
        if self.available:
            return "Available"
        return f"Checked out to {self.borrower}"


collection = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565",
         1925, "Classic Fiction"),
    Book("Educated", "Tara Westover", "978-0399590504", 2018, "Memoir"),
    Book("Dune", "Frank Herbert", "978-0441013593", 1965, "Science Fiction"),
    Book("The Nickel Boys", "Colson Whitehead", "978-0385537070",
         2019, "Historical Fiction"),
    Book("Thinking in Systems", "Donella Meadows", "978-1603580557",
         2008, "Nonfiction"),
    Book("Beloved", "Toni Morrison", "978-1400033416", 1987, "Literary Fiction"),
]

print("=== Full Collection ===")
for book in collection:
    print(book)

print("\n=== Checkouts ===")
if collection[0].check_out("Jordan"):
    print(f"'{collection[0].title}' checked out to Jordan.")
else:
    print(f"'{collection[0].title}' is already checked out.")

if collection[1].check_out("Priya"):
    print(f"'{collection[1].title}' checked out to Priya.")
else:
    print(f"'{collection[1].title}' is already checked out.")

if collection[0].check_out("Marcus"):
    print(f"'{collection[0].title}' checked out to Marcus.")
else:
    print(f"'{collection[0].title}' is already checked out.")

print("\n=== Returns ===")
print(collection[1].return_book())

print("\n=== Sorted by Title ===")
for book in sorted(collection, key=lambda b: b.title):
    print(book)

print("\n=== Available Books ===")
available_books = [book for book in collection if book.available]
for book in available_books:
    print(book)