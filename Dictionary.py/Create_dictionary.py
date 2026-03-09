d = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = int(input("Enter key: "))
    value = int(input("Enter value: "))
    d[key] = value

print("Dictionary:", d)

print("Maximum Key:", max(d.keys()))
print("Maximum Value:", max(d.values()))