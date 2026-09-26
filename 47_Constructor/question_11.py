# Question:
# Create a class Playlist where __init__ accepts *args as initial songs.
# Store them in a list and allow adding more songs.

class Playlist:
    def __init__(self, *songs):
        self.songs = list(songs)  # *args in constructor

    def add(self, song):
        self.songs.append(song)

    def display(self):
        print(f"Playlist ({len(self.songs)} songs):")
        for i, song in enumerate(self.songs, 1):
            print(f"  {i}. {song}")

# Create with initial songs using *args
p = Playlist("Song A", "Song B", "Song C")
p.display()

p.add("Song D")
p.add("Song E")
p.display()
