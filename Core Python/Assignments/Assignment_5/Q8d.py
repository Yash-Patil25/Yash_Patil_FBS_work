#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = float(input("Enter value of a: "))

sum_series = 0
for i in range(1, 11):
    sum_series += (a ** i) / i

print("Sum of series (a + a^2/2 + ... + a^10/10) =", sum_series)
