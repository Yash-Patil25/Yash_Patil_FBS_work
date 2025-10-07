#Write a program to reverse three-digit number.
num = int(input("enter three digit no:"))

hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

reversed_num = (units * 100) + (tens * 10) + hundreds
print("Reversed number:",reversed_num)