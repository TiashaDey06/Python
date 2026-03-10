s = input("Enter a string: ")

s = s.lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

flag = True

for ch in alphabet:
    if ch not in s:
        flag = False
        break

if flag:
    print("The string is a Pangram")
else:
    print("The string is not a Pangram")