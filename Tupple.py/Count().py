n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

t = tuple(lst)

x = int(input("Enter element to count: "))

print("Tuple:", t)
print("Count of", x, "is:", t.count(x))