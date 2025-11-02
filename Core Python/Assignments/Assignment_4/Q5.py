#WAP to print Fibonacci series upto n.
n = int(input("Enter Number:"))

a, b = 0, 1
print("Fibonacci series up to",n, "terms:")

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c