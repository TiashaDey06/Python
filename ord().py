# Find ASCII Value of any character using ord()function

ch = input("Enter a character: ")

if len(ch) == 1:
    print("ASCII value:", ord(ch))
else:
    print("Please enter only one character")


# Find Alphabet Value of any character using ord()function

ch = input("Enter an alphabet: ")

value = ord(ch.lower()) - 96     # both uppercase and lowercase

print("Alphabet value:", value)