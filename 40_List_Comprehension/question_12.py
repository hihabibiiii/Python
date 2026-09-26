# Question:
# Extract all vowels from a string using list comprehension.

text = input("Enter a string: ")
vowels = [ch for ch in text if ch.lower() in "aeiou"]

print(f"String: '{text}'")
print(f"Vowels: {vowels}")
print(f"Count:  {len(vowels)}")
