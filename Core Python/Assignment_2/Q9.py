#Write a program to swap two numbers without using third variable.
a = int(input("Enter first no:"))
b = int(input("Enter second no:"))

print("\nBefore swapping: a =",a,"b =",b)

a = a + b
b = a - b
c = a - b

print("Ater swapping: a =",a,"b =",b)