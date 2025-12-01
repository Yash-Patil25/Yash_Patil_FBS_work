#Write a program to print Fibonacci series using recursion.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

num = int(input("Enter number of terms: "))

print("Fibonacci series:")
for i in range(num):
    print(fib(i), end=" ")

