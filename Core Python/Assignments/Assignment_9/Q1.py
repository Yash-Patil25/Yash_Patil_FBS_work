#Write a program to find sum of following series using recursive functions:

#i. 1! + 2! + 3! + 4! +..... + n!
#Note : For fact and sum two recursive functions

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def series_sum(n):
    if n == 1:
        return fact(1)
    return fact(n) + series_sum(n - 1)

n = int(input("Enter value of n: "))
print("Sum of series 1! + 2! + ... +",n,"!=",series_sum(n))