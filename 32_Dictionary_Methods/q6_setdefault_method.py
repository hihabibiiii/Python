# Question 6 (Medium):
# Use the setdefault() method to add a key only if it doesn't already exist.
# Demonstrate that setdefault() does NOT overwrite existing values.

# Solution:
config = {
    "theme": "dark",
    "font_size": 14
}

print("Original config:", config)

# setdefault() adds 'language' because it doesn't exist
config.setdefault("language", "English")
print("\nAfter setdefault('language', 'English'):", config)

# setdefault() does NOT overwrite 'theme' because it already exists
config.setdefault("theme", "light")  # 'dark' stays
print("After setdefault('theme', 'light'):", config)

# Practical: ensure a default value exists before using it
config.setdefault("max_connections", 100)
print(f"\nMax connections: {config['max_connections']}")

# Example Output:
# Original config: {'theme': 'dark', 'font_size': 14}
# After setdefault('language', 'English'): {'theme': 'dark', 'font_size': 14, 'language': 'English'}
# After setdefault('theme', 'light'):      {'theme': 'dark', 'font_size': 14, 'language': 'English'}
# Max connections: 100
