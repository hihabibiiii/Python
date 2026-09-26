# Question:
# Override __len__ to return a meaningful length for a custom class.

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = text.split()

    def __len__(self):
        return len(self.words)  # Length = number of words

    def __str__(self):
        return f"Sentence: '{self.text}'"

class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __len__(self):
        return len(self.members)  # Length = number of members

    def __str__(self):
        return f"Team '{self.name}': {self.members}"

s = Sentence("Python is great for beginners")
t = Team("Dev Team", ["Alice", "Bob", "Charlie", "Diana"])

print(s)
print(f"len(sentence) = {len(s)} words")
print()
print(t)
print(f"len(team) = {len(t)} members")
