#Write a program to input angles of a triangle and check whether triangle is valid or not.
angle1 = float(input("Enter angle:"))
angle2 = float(input("Enter angle:"))
angle3 = float(input("Enter angle:"))

if angle1 > 0 and angle2 > 0 and angle3 > 0 and (angle1+angle2+angle3 == 180):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
