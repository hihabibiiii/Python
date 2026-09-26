# Question: Use partition() and rpartition() to split a string on a separator.
# partition(sep)  -> splits at FIRST occurrence of sep -> (before, sep, after)
# rpartition(sep) -> splits at LAST  occurrence of sep -> (before, sep, after)
# Example:
#   String: "one:two:three"
#   partition(':')  -> ('one', ':', 'two:three')
#   rpartition(':') -> ('one:two', ':', 'three')

text = input("Enter a string: ")
sep = input("Enter the separator: ")

part_result = text.partition(sep)
rpart_result = text.rpartition(sep)

print(f"\npartition('{sep}'):")
print(f"  Before: '{part_result[0]}'")
print(f"  Sep:    '{part_result[1]}'")
print(f"  After:  '{part_result[2]}'")

print(f"\nrpartition('{sep}'):")
print(f"  Before: '{rpart_result[0]}'")
print(f"  Sep:    '{rpart_result[1]}'")
print(f"  After:  '{rpart_result[2]}'")
