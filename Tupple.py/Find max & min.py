n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    num = int(input("Enter number: "))
    lst.append(num)

t = tuple(lst)

print("Tuple:", t)
print("Maximum value:", max(t))
print("Minimum value:", min(t))