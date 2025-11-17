#Write a program to find sum of following series using functions :
#a.1+ 2 + 3 + 4+..... + n
def sum_of_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = int(input("Enter the value of n:"))

result = sum_of_series(n)

print("The sum of the series 1 + 2 + 3 +...+",n,"is:",result)