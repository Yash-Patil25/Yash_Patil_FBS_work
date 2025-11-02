#Looping.
#WAP to print all even numbers until n.
n = int(input("Enter the value of n:"))

print("Even numbers from 1 to",n,"are:")
for i in range(2, n+1, 2):
    print(i)