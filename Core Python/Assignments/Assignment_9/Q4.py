#Write a program to find sum of n numbers using recursion.

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

num = int(input("Enter value of n: "))
print("Sum of first", num, "numbers is:", sum_n(num))
