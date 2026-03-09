n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

t = tuple(lst)

x = int(input("Enter element to find index: "))

print("Tuple:", t)
print("Index of", x, "is:", t.index(x))