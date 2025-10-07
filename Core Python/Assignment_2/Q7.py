#Find the sum of three-digit number.
num = int(input("Enter three-digits number:"))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

sum_of_digits = hundreds + tens + ones

print("sum of digits =",sum_of_digits)