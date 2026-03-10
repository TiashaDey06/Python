# Reverse a list in-place without using another list or built-in reverse.

L = [1,2,3,4,5]

n = len(L)

for i in range(n//2):
    temp = L[i]
    L[i] = L[n-1-i]
    L[n-1-i] = temp

print(L)