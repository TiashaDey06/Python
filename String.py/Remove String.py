# write a python program to Remove adjacent duplicate character pairs from a string repeatedly. Ex: 'aaabccddd' → 'abd', 'abba' → 'Empty String'


s = input("Enter a string: ")

stack = []

for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()        # remove the pair
    else:
        stack.append(ch)   # add character

result = "".join(stack)

if result == "":
    print("Empty String")
else:
    print("Result:", result)