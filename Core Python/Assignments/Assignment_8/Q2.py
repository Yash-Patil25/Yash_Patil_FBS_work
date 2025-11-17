#Write a program to calculate area of circle

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area

radius = float(input("Enter area of circle:"))

area = area_of_circle(radius)

print("The area of the circle is:",area)