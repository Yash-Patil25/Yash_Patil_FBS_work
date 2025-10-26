#WAP to calculate area of triangle and rectangle.

#Area of triangle
base = float(input("Enter base of triangle:"))
height = float(input("Enter height of triangle:"))

triangle_area = 0.5 * base * height

print("Area of triangle =",triangle_area)

#Area of rectangle.
length = float(input("Enter length of rectangle:"))
breadth = float(input("Enter breadth of rectangle:"))

rectangle_area = length * breadth

print("Area of rectangle =",rectangle_area)