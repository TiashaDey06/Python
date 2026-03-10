# Without Recursion (Using Loop)

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


# With Recursion 

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter number of terms: "))

for i in range(n):
    print(fib(i), end=" ")