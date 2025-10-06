#Write a program to enter P, T, R and calculate simple Interest.
P = float(input("Enter pricipal amount:"))
T = float(input("Enter Time (in years):"))
R = float(input("Enter Rate of interest:"))

SI = (P * R * T)/100

print(f'Simple Interest is {SI}.')