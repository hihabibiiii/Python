# Question:
# Override __str__ in multiple classes and demonstrate how print() behaves
# polymorphically.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Book: '{self.title}' by {self.author}"

class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
    def __str__(self):
        return f"Movie: '{self.title}' directed by {self.director}"

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
    def __str__(self):
        return f"Song: '{self.title}' by {self.artist}"

media = [
    Book("Python Crash Course", "Eric Matthes"),
    Movie("Inception", "Christopher Nolan"),
    Song("Bohemian Rhapsody", "Queen"),
]

for item in media:
    print(item)  # Uses each class's __str__
