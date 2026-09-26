# Question: Create a class Library with a list of books.
# Add methods add_book() and display_books().

# Example output:
# === City Library ===
# Book added: 'Python Crash Course'
# Book added: '1984'
# Book added: 'The Great Gatsby'
# 
# Books in library:
# 1. Python Crash Course
# 2. 1984
# 3. The Great Gatsby
# Total books: 3

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # list attribute to hold books

    def add_book(self, book_title):
        self.books.append(book_title)
        print(f"Book added: '{book_title}'")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
            return
        print(f"\nBooks in {self.name}:")
        for i, book in enumerate(self.books, 1):
            print(f"  {i}. {book}")
        print(f"Total books: {len(self.books)}")

    def remove_book(self, book_title):
        if book_title in self.books:
            self.books.remove(book_title)
            print(f"Book removed: '{book_title}'")
        else:
            print(f"Book '{book_title}' not found.")

# Create library and add books
library = Library("City Library")
print(f"=== {library.name} ===")
library.add_book("Python Crash Course")
library.add_book("1984")
library.add_book("The Great Gatsby")

library.display_books()

library.remove_book("1984")
library.display_books()
