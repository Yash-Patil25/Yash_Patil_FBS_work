#Write a program to swap two numbers using third variable.
a = int(input("Enter first no:"))
b = int(input("Enter second no:"))

print("\nBefore swapping: a =",a,"b =",b)

temp = a
a = b
b = temp

print("After Swapping: a =",a,"b =",b)