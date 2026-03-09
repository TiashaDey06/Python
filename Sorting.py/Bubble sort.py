n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array :", arr)