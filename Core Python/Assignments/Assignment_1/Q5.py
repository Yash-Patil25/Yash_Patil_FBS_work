#Write a program to enter P, T, R and calculate Compound Interest.
P = float(input("Enter principle amount:"))
T = float(input("Enter Time(in yrs):"))
R = float(input("Enter Rate of interest:"))

A = P * (1 + R / 100) ** T  #final amount
CI = A - P      #compound interest

print("Compound Interest = ",CI)
print("Total Amount = ",A)