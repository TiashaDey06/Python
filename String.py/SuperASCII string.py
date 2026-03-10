s = input("Enter a string: ")

total = 0

for ch in s:
    total = total + ord(ch)

if total == len(s) * 100:
    print("Super ASCII String")
else:
    print("Not a Super ASCII String")