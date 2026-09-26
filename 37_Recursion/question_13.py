# Question:
# Write a recursive function to generate all subsets of a list.
# subsets([1,2,3]) = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

def subsets(lst):
    if len(lst) == 0:
        return [[]]
    first = lst[0]
    rest = subsets(lst[1:])
    return rest + [[first] + s for s in rest]

data = [1, 2, 3]
result = subsets(data)
print(f"Subsets of {data}:")
for s in result:
    print(f"  {s}")
print(f"Total subsets: {len(result)}")
