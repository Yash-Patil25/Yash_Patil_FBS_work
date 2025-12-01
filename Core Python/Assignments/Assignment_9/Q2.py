#Write a program to check if given number is Armstrong or not using recursive function.

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def power(d, p):
    if p == 0:
        return 1
    return d * power(d, p - 1)

def armstrong_sum(n, p):
    if n == 0:
        return 0
    digit = n % 10
    return power(digit, p) + armstrong_sum(n // 10, p)

num = int(input("Enter a number: "))
digits = count_digits(num)
result = armstrong_sum(num, digits)

if result == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
