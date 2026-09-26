# Question: Access object attributes using dot notation (object.attribute).
# Create a Book class and access its attributes using dot notation.

# Example output:
# Title:     The Alchemist
# Author:    Paulo Coelho
# Pages:     197
# Published: 1988
# book1.title → "The Alchemist"

class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

# Create a book object
book1 = Book("The Alchemist", "Paulo Coelho", 197, 1988)

# Access attributes using DOT NOTATION: object.attribute
print(f"Title:     {book1.title}")
print(f"Author:    {book1.author}")
print(f"Pages:     {book1.pages}")
print(f"Published: {book1.year}")

print(f'\nbook1.title → "{book1.title}"')
print(f"book1.pages → {book1.pages}")

# Create another book and access its attributes
book2 = Book("1984", "George Orwell", 328, 1949)
print(f"\nSecond book: {book2.title} by {book2.author} ({book2.year})")
