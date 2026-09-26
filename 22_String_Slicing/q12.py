# Question: Take a string and print it in 3-character chunks using slicing in a loop.
# Example:
#   Input: "programming"
#   Output:
#     pro
#     gra
#     mmi
#     ng

text = input("Enter a string: ")
chunk_size = 3
print("String in 3-character chunks:")
for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    print(chunk)
