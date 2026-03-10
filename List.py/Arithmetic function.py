# Find arithmetic mean, variance and standard deviation of a list.

L = [2,4,6,8]

n = len(L)

# mean
sum1 = 0
for i in L:
    sum1 = sum1 + i
mean = sum1 / n

# variance
sum2 = 0
for i in L:
    sum2 = sum2 + (i - mean) * (i - mean)
variance = sum2 / n

# standard deviation
sd = variance ** 0.5

print("Mean =", mean)
print("Variance =", variance)
print("Standard Deviation =", sd)