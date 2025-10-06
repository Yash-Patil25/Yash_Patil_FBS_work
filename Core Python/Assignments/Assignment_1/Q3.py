#Program to find quotient and remainder of two numbers.

dividend = int(input("Enter dividend:"))
divisor = int(input("Enter divisor:"))

quotient = dividend // divisor

remainder = dividend % divisor

print("Quotient is",quotient)
print("Remainder is",remainder)