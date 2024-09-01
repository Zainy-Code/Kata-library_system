import unittest
from library import Library, Book


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        book1 = Book("ISBN123", "Book 1", "Author 1", 2023)
        book2 = Book("ISBN456", "Book 2", "Author 2", 2024)

        self.assertTrue(self.library.add_book(book1))
        self.assertTrue(self.library.add_book(book2))
        self.assertFalse(self.library.add_book(book1))  # Test duplicate add

    def test_borrow_book(self):
        book = Book("ISBN123", "Book 1", "Author 1", 2023)
        self.library.add_book(book)

        self.assertTrue(self.library.borrow_book("ISBN123"))
        self.assertFalse(self.library.borrow_book("ISBN123"))  # Test borrowing unavailable book

    def test_return_book(self):
        book = Book("ISBN123", "Book 1", "Author 1", 2023)
        self.library.add_book(book)
        self.library.borrow_book("ISBN123")

        self.assertTrue(self.library.return_book("ISBN123"))
        self.assertFalse(self.library.return_book("ISBN123"))  # Test returning already available book

    def test_view_available_books(self):
        book1 = Book("ISBN123", "Book 1", "Author 1", 2023)
        book2 = Book("ISBN456", "Book 2", "Author 2", 2024)
        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.borrow_book("ISBN123")

        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0].isbn, "ISBN456")  # Check available book


if __name__ == "__main__":
    unittest.main()