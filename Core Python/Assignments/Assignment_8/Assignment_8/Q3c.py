#c.1^1 + 2^2 + 3^3+ ...... n^n

def sum_of_power_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

n = int(input("Enter the value of n: "))

result = sum_of_power_series(n)

print("The sum of the series 1^1 + 2^2 + 3^3 + ... +", n, "^", n, "is:", result)
