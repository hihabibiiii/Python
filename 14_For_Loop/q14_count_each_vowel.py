# Question:
# Take a string from the user.
# Count the occurrences of each vowel (a, e, i, o, u) using a for loop.
# Use separate variables: a_count, e_count, i_count, o_count, u_count.
#
# Example:
#   Input: "Hello Beautiful World"
#   Output:
#     a_count: 1
#     e_count: 3
#     i_count: 1
#     o_count: 2
#     u_count: 1

text = input("Enter a string: ").lower()

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

for char in text:
    if char == 'a':
        a_count = a_count + 1
    if char == 'e':
        e_count = e_count + 1
    if char == 'i':
        i_count = i_count + 1
    if char == 'o':
        o_count = o_count + 1
    if char == 'u':
        u_count = u_count + 1

print(f"\nVowel counts in '{text}':")
print(f"  a_count: {a_count}")
print(f"  e_count: {e_count}")
print(f"  i_count: {i_count}")
print(f"  o_count: {o_count}")
print(f"  u_count: {u_count}")
