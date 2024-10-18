# References
# https://www.w3schools.com/python/python_classes.asp
# https://www.youtube.com/watch?v=yZUL7IFA324 
# https://github.com/Uthpal-p/Library-Management-system-using-Python/blob/main/main_lms.py
# https://k4y0x13.github.io/CSF101-Programming-Methodology/OOP/Worksheet2.html

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # This book is available for borrowing
        self.borrowed_by = None  # Keeps track of who borrowed the book

    def __str__(self):
        # Display the book's title, author, and its availability status
        status = "Available" if self.available else f"Currently borrowed by {self.borrowed_by.name}"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.collection = {}  # A dictionary to hold books, indexed by their title

    def add_book(self, book):
        # Add a new book to the library's collection
        self.collection[book.title] = book

    def view_books(self):
        # Show all books in the library
        if not self.collection:
            print("Oops! No books are available in the library right now.")
            return
        print("Here are the available books in the library:")
        for book in self.collection.values():
            print(book)

    def borrow_book(self, title, user):
        # Allow a user to borrow a book from the library
        if title in self.collection:
            book = self.collection[title]
            if book.available:
                book.available = False
                book.borrowed_by = user
                user.borrowed_books.append(book)
                print(f"{user.name} has successfully borrowed: {book.title}")
            else:
                print(f"Sorry, '{title}' is currently borrowed by {book.borrowed_by.name}.")
        else:
            print(f"Sorry, the book titled '{title}' doesn't exist in our library.")

    def return_book(self, title, user):
        # Allow a user to return a borrowed book
        for book in user.borrowed_books:
            if book.title == title:
                book.available = True
                book.borrowed_by = None
                user.borrowed_books.remove(book)
                print(f"{user.name} has returned: {book.title}")
                return
        print(f"{user.name} doesn't have the book '{title}' borrowed.")


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # A list to keep track of books borrowed by the user

    def borrow(self, library, title):
        # User borrows a book from the library
        library.borrow_book(title, self)

    def return_book(self, library, title):
        # User returns a book to the library
        library.return_book(title, self)


class Admin(User):
    def add_book(self, library, title, author):
        # Admin adds a new book to the library
        new_book = Book(title, author)
        library.add_book(new_book)
        print(f"Admin {self.name} has added '{title}' by {author} to the library collection.")

    def borrow(self, library, title):
        # Admin cannot borrow books
        print(f"Admin {self.name} cannot borrow books. But feel free to manage the library!")

    def track_borrowed_books(self, library):
        # Admin checks which books are currently borrowed
        print("Let's see which books are borrowed:")
        borrowed_books = [book for book in library.collection.values() if not book.available]
        if not borrowed_books:
            print("Great news! No books are currently borrowed.")
        else:
            for book in borrowed_books:
                print(f"{book.title} is borrowed by {book.borrowed_by.name}")


def main():
    library = Library()  # Create a new library instance
    admin = Admin("Admin")  # Create an admin user
    users = {}  # A dictionary to keep track of users

    while True:
        print("\n--- Welcome to the Library System ---")
        print("1. Log in as Admin")
        print("2. Log in as User")
        print("3. Exit the system")

        choice = input("Please enter your choice: ")

        if choice == '1':
            # Admin functionalities
            while True:
                print("\n--- Admin Menu ---")
                print("1. View Books")
                print("2. Add a Book")
                print("3. Track Borrowed Books")
                print("4. Log Out")

                admin_choice = input("What would you like to do? ")

                if admin_choice == '1':
                    library.view_books()

                elif admin_choice == '2':
                    book_title = input("Please enter the title of the book: ")
                    book_author = input("Please enter the author's name: ")
                    admin.add_book(library, book_title, book_author)

                elif admin_choice == '3':
                    admin.track_borrowed_books(library)

                elif admin_choice == '4':
                    print("Logging out from Admin Menu. Thank you for managing the library!")
                    break

                else:
                    print("Oops! That choice isn't valid. Please try again.")

        elif choice == '2':
            # User functionalities
            user_name = input("Welcome! Please enter your name: ")
            if user_name not in users:
                users[user_name] = User(user_name)
            user = users[user_name]

            while True:
                print(f"\n--- User Menu for {user.name} ---")
                print("1. View Available Books")
                print("2. Borrow a Book")
                print("3. Return a Book")
                print("4. Log Out")

                user_choice = input("What would you like to do? ")

                if user_choice == '1':
                    library.view_books()

                elif user_choice == '2':
                    book_title = input("What is the title of the book you want to borrow? ")
                    user.borrow(library, book_title)

                elif user_choice == '3':
                    book_title = input("What is the title of the book you want to return? ")
                    user.return_book(library, book_title)

                elif user_choice == '4':
                    print(f"Logging out as {user.name}. Thank you for visiting the library!")
                    break

                else:
                    print("Oops! That choice isn't valid. Please try again.")

        elif choice == '3':
            print("Thank you for using the library system. Goodbye!")
            break

        else:
            print("Oops! That choice isn't valid. Please try again.")

if __name__ == "__main__":
    main()