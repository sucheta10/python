# Library Management System
# Design a simple library management system using Python classes and objects. The system should be able to handle the addition and removal of books, track who borrows what book, and maintain a list of books currently available in the library.
# Requirements:
# * Create a class Book that stores information about each book: title, author, and ISBN.
# * Create a class Library that maintains a collection of books and can add books, remove books, and lend books to users.
# * The Library class should also be able to display all books currently available and a list of books that are borrowed along with the names of the borrowers.
# * Implement methods in the Library class for add_book, remove_book, and borrow_book.

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrower = None

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                self.books.remove(book)
                print(f"{book.title} has been removed from the library.")
                return
        print("Book not found in the library.")

    def borrow_book(self, book_title, borrower):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.borrower is None:
                    book.borrower = borrower
                    print(f"{borrower} has borrowed {book.title}.")
                else:
                    print("Sorry, the book is already borrowed.")
                return
        print("Book not found in the library.")

    def display_available_books(self):
        print("Available Books:")
        available_books = [book for book in self.books if book.borrower is None]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available in the library.")

    def display_borrowed_books(self):
        print("Borrowed Books:")
        borrowed_books = [book for book in self.books if book.borrower is not None]
        if borrowed_books:
            for book in borrowed_books:
                print(f"{book} - Borrower: {book.borrower}")
        else:
            print("No books are currently borrowed.")

# Function to prompt user for book details
def input_book_details():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    return title, author, isbn

# Function to prompt user for borrower's name
def input_borrower_name():
    return input("Enter your name: ")


def main():
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Remove Book")
        print("3. Borrow Book")
        print("4. Display Available Books")
        print("5. Display Borrowed Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title, author, isbn = input_book_details()
            new_book = Book(title, author, isbn)
            library.add_book(new_book)

        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)

        elif choice == '3':
            title = input("Enter the title of the book to borrow: ")
            borrower = input_borrower_name()
            library.borrow_book(title, borrower)

        elif choice == '4':
            library.display_available_books()

        elif choice == '5':
            library.display_borrowed_books()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

main()
