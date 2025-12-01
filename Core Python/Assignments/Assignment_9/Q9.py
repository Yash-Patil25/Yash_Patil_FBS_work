#Write a program to calculate the m to the power n using recursion.

def power(m, n):
    if n == 0:          
        return 1
    return m * power(m, n - 1)  

# Main program
m = int(input("Enter base (m): "))
n = int(input("Enter exponent (n): "))

print(m, "to the power", n, "is:", power(m, n))
