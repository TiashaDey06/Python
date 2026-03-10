# Add corresponding elements of two equal-size lists L and M to form N. Ex: L=[3,1,4], M=[1,5,9] → N=[4,6,13]

L = [3, 1, 4]
M = [1, 5, 9]

N = []

for i in range(len(L)):
    N.append(L[i] + M[i])

print("List N:", N)