import unittest

from CSF101_CAP2_02230304 import Library, Admin, User

class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        # Setup a new library and admin for each test
        self.library = Library()
        self.admin = Admin("Admin")
        self.user1 = User("User1")
        self.user2 = User("User2")

    def test_valid_book_borrowing(self):
        # Admin adds a book
        self.admin.add_book(self.library, "The Great Gatsby", "F. Scott Fitzgerald")
        
        # User1 borrows the book
        self.user1.borrow(self.library, "The Great Gatsby")
        
        # Check if the book is now marked as borrowed
        book = self.library.collection["The Great Gatsby"]
        self.assertFalse(book.available)
        self.assertEqual(book.borrowed_by, self.user1)
        
    def test_invalid_book_borrowing(self):
        # Admin adds a book
        self.admin.add_book(self.library, "1984", "George Orwell")
        
        # User1 borrows the book
        self.user1.borrow(self.library, "1984")
        
        # User2 tries to borrow the same book
        self.user2.borrow(self.library, "1984")
        
        # Check if the book is still marked as borrowed by User1
        book = self.library.collection["1984"]
        self.assertFalse(book.available)
        self.assertEqual(book.borrowed_by, self.user1)

    def test_valid_book_returning(self):
        # Admin adds a book
        self.admin.add_book(self.library, "Moby Dick", "Herman Melville")
        
        # User1 borrows the book
        self.user1.borrow(self.library, "Moby Dick")
        
        # User1 returns the book
        self.user1.return_book(self.library, "Moby Dick")
        
        # Check if the book is now available again
        book = self.library.collection["Moby Dick"]
        self.assertTrue(book.available)
        self.assertIsNone(book.borrowed_by)

    def test_invalid_book_returning(self):
        # Admin adds a book
        self.admin.add_book(self.library, "To Kill a Mockingbird", "Harper Lee")
        
        # User1 tries to return a book they haven't borrowed
        initial_borrowed_books = len(self.user1.borrowed_books)
        self.user1.return_book(self.library, "To Kill a Mockingbird")
        
        # Check if the borrowed_books list hasn't changed
        self.assertEqual(len(self.user1.borrowed_books), initial_borrowed_books)

    def test_admin_adding_books(self):
        # Admin adds a new book
        self.admin.add_book(self.library, "Pride and Prejudice", "Jane Austen")
        
        # Check if the book is in the library collection
        self.assertIn("Pride and Prejudice", self.library.collection)
        book = self.library.collection["Pride and Prejudice"]
        self.assertEqual(book.title, "Pride and Prejudice")
        self.assertEqual(book.author, "Jane Austen")
        self.assertTrue(book.available)

    def test_edge_case_borrow_all_books(self):
        # Admin adds multiple books
        self.admin.add_book(self.library, "Book1", "Author1")
        self.admin.add_book(self.library, "Book2", "Author2")
        
        # User1 borrows all books
        self.user1.borrow(self.library, "Book1")
        self.user1.borrow(self.library, "Book2")
        
        # Check if all books are now unavailable
        for book in self.library.collection.values():
            self.assertFalse(book.available)

    def test_edge_case_return_non_borrowed_book(self):
        # Admin adds a book
        self.admin.add_book(self.library, "Frankenstein", "Mary Shelley")
        
        # User1 borrows the book
        self.user1.borrow(self.library, "Frankenstein")
        
        # User2 tries to return the book they haven't borrowed
        initial_borrowed_books = len(self.user2.borrowed_books)
        self.user2.return_book(self.library, "Frankenstein")
        
        # Check that the borrowed_books list of user2 hasn't changed
        self.assertEqual(len(self.user2.borrowed_books), initial_borrowed_books)
        
        # Check that the book is still marked as borrowed by User1
        book = self.library.collection["Frankenstein"]
        self.assertFalse(book.available)
        self.assertEqual(book.borrowed_by, self.user1)

if __name__ == '__main__':
    unittest.main()
