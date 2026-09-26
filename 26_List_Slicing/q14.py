# Question: Compare two sublists using slicing — check if the first half equals
#           the reversed second half (i.e., the list is a palindrome list).
# Example:
#   Palindrome list:     [1, 2, 3, 2, 1]
#   Non-palindrome list: [1, 2, 3, 4, 5]

def check_palindrome_list(lst):
    mid = len(lst) // 2
    first_half = lst[:mid]
    second_half = lst[mid + len(lst) % 2:]  # skip middle element if odd length
    return first_half == second_half[::-1]

list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]

print("List:", list1)
print("Is palindrome list?", check_palindrome_list(list1))

print("\nList:", list2)
print("Is palindrome list?", check_palindrome_list(list2))
