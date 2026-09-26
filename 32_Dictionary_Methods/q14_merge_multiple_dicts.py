# Question 14 (Hard):
# You have a list of dictionaries. Each dictionary represents additional settings.
# Merge all of them into one master dictionary using update() in a loop.
# Print the final merged result.

# Solution:
master = {}

settings_list = [
    {"theme": "dark", "language": "English"},
    {"font_size": 14, "font_family": "Arial"},
    {"show_toolbar": True, "auto_save": True},
    {"timeout": 30, "max_retries": 3},
    {"version": "2.1.0", "debug": False}
]

print("Merging dictionaries one by one:\n")
for i, settings in enumerate(settings_list, start=1):
    master.update(settings)
    print(f"After merging dict {i}: {master}")

print("\nFinal merged dictionary:")
for key, value in master.items():
    print(f"  {key}: {value}")

# Example Output:
# After merging dict 1: {'theme': 'dark', 'language': 'English'}
# After merging dict 2: {'theme': 'dark', 'language': 'English', 'font_size': 14, 'font_family': 'Arial'}
# ...
# Final merged dictionary:
#   theme: dark
#   language: English
#   ...
