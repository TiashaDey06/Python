octal = input("Enter an octal number: ")

decimal = int(octal, 8)
binary = bin(decimal)[2:]

print("Binary number is:", binary)