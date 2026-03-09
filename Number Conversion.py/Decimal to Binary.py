num = int(input("Enter a decimal number: "))

binary = ""

while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num = num // 2

print("Binary number is:", binary)