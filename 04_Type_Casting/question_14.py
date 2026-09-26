# Question 14 (Hard):
# Start with a mixed-type list: [1, '2', 3.0, True]
# Convert every element to a string.
# Join them together into a single string and print it.

# Solution:
mixed_list = [1, '2', 3.0, True]
print("Original list:", mixed_list)

string_list = []
for item in mixed_list:
    string_list.append(str(item))

print("All as strings:", string_list)
joined = " ".join(string_list)
print("Joined string :", joined)

# Output:
# Original list: [1, '2', 3.0, True]
# All as strings: ['1', '2', '3.0', 'True']
# Joined string : 1 2 3.0 True
