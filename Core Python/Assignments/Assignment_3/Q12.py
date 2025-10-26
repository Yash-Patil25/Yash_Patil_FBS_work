# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3-three digit no:"))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

if hundreds == ones:
    print(num,"is a pallindrome.")
else:
    print(num,"is not pallindrome.")
