#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)

N = int(input("Enter number N: "))

sum_series = 0
for i in range(1, N + 1):
    sum_series += N ** i

print("Sum of series (N + N^2 + ... + N^N) =", sum_series)
