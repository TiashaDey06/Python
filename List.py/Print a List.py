# create a list using a loop: "the list['a','bb','ccc',...] that ends with 26 copies of z"

lst = []

for i in range(1, 27):
    lst.append(chr(96 + i)* i)

print(lst)