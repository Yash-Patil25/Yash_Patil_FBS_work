#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input("Enter number of terms: "))

sum_series = 0
term = 1

for i in range(1, n + 1):
    sum_series += term
    term *= 2

print("Sum of geometric series =", sum_series)
