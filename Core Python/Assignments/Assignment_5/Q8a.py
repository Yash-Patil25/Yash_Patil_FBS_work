#Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!

n = int(input("Enter value of n: "))

sum_series = 0

fact = 1
for i in range(1, n + 1):
    fact *= i          
    sum_series += fact

print("Sum of series (1! + 2! + ... + n!) =", sum_series)
