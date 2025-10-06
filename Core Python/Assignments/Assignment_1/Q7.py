#Program to Find the Roots of a Quadratic Equation

import math
a = float(input("Enter coefficient a:"))
b = float(input("Enter coefficient b:"))
c = float(input("Enter coefficient c:"))

#calculate discriminant
d = (b ** 2) - (4 * a * c)

#check the nature of the roots
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are real and different.")
    print("Root 1 = ",root1)
    print("Root 2 = ",root2)
elif d == 0:
    root = -b / (2 * a)
    print("Roots are real and equal")
    print("Root 1 = Root 2 =",root)
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(d)) / (2 * a)
    print("Roots are complex and different")
    print(f'Root 1 = {real_part} + {imaginary_part}i')
    print(f'Root 2 = {real_part} + {imaginary_part}i')