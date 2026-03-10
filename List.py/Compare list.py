# Compare two equal-sized lists and print the first index where they differ.

L = [1,2,3,4,5]
M = [1,2,0,4,5]

for i in range(len(L)):
    if L[i] != M[i]:
        print("First different index:", i)
        break