binary = input("Enter a binary number: ")

decimal = int(binary, 2)
octal = oct(decimal)[2:]

print("Octal number is:", octal)