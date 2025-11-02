#WAP to check if a given number is prime number or not.
n = int(input("Enter Number:"))

if n > 1:
    for i in range(2,n):
        if n % i == 0:
            print(n,"is a not prime")
            break
    else:
            print(n,"is a prime")
else:
     print(n,"is not a prime")