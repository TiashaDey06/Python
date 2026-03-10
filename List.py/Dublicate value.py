# Move all duplicate values in a list to the end.

lst = [1, 2, 3, 2, 4, 1, 5]

unique = []
duplicate = []

for x in lst:
    if x not in unique:
        unique.append(x)
    else:
        duplicate.append(x)

result = unique + duplicate

print("Result:", result)