#functions.
#Write a program to calculate area of rectangle

def area_of_rec(length, breadth):
    area = length * breadth
    return area

length = float(input("Enter the length of rectangle:"))
breadth = float(input("Enter the breadth of rectangle:"))

area = area_of_rec(length, breadth)
print("Area of rectangle is:",area)

