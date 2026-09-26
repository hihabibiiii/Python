# Question: Use startswith() and endswith() to check a filename.
# startswith() checks if the string begins with a given prefix.
# endswith() checks if the string ends with a given suffix.
# Example:
#   Filename: "report_2024.pdf"
#   Output: Starts with 'report': True
#           Ends with '.pdf': True

filename = input("Enter a filename (e.g., report_2024.pdf): ")

starts = filename.startswith("report")
ends = filename.endswith(".pdf")

print(f"Starts with 'report': {starts}")
print(f"Ends with '.pdf': {ends}")

if starts and ends:
    print("This is a valid report PDF file.")
else:
    print("This file may not be a report PDF.")
