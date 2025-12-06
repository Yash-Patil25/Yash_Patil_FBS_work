#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

n = int(input("Enter the value of n:"))

result = {}

for x in range(1, n + 1):
    result[x] = x * x

print("Generated Dictionary:",result)