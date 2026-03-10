num = int(input("Enter a number: "))

flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
        break

if flag and num > 1:
    print("Prime number")
else:
    print("Not a prime number")


# Reverse Prime program

num = int(input("Enter a number: "))

rev = int(str(num)[::-1])

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return n > 1

if prime(num) and prime(rev):
    print("Reverse Prime Number")
else:
    print("Not a Reverse Prime Number")