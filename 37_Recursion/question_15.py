# Question:
# Write a recursive function to generate all permutations of a string.
# permutations("abc") = ["abc", "acb", "bac", "bca", "cab", "cba"]

def permutations(s):
    if len(s) <= 1:
        return [s]
    result = []
    for i, ch in enumerate(s):
        remaining = s[:i] + s[i+1:]
        for perm in permutations(remaining):
            result.append(ch + perm)
    return result

text = input("Enter a string (max 5 chars recommended): ")
perms = permutations(text)
print(f"All permutations of '{text}':")
for p in perms:
    print(f"  {p}")
print(f"Total: {len(perms)}")
