#Write a program to find print the following Fibonacci series using
#functions:
#1 1 2 3 5 8 n terms.

def fibonacci_series(n):
    a, b = 1, 1
    print(a, b, end=" ")
    for _ in range(2, n):
        next_term = a + b
        print(next_term, end=" ")
        a, b = b, next_term

n = int(input("Enter the number of term:"))
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("1")
else:
    print("Fibonacci series up to",n,"terms:")
    fibonacci_series(n)