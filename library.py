class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            return True
        else:
            return False

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                book.is_available = False
                return True
        return False

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_available:
                book.is_available = True
                return True
        return False

    def view_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        return available_books

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View Available Books")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            publication_year = int(input("Enter publication year: "))
            book = Book(isbn, title, author, publication_year)
            if library.add_book(book):
                print("Book added successfully.")
            else:
                print("Book already exists.")
        elif choice == 2:
            isbn = input("Enter ISBN of the book to borrow: ")
            if library.borrow_book(isbn):
                print("Book borrowed successfully.")
            else:
                print("Book not found or unavailable.")
        elif choice == 3:
            isbn = input("Enter ISBN of the book to return: ")
            if library.return_book(isbn):
                print("Book returned successfully.")
            else:
                print("Book not found or already available.")
        elif choice == 4:
            available_books = library.view_available_books()
            if available_books:
                print("Available Books:")
                for book in available_books:
                    print(f"ISBN: {book.isbn}, Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
            else:
                print("No books available.")
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()