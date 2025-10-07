#Convert distant given in feet and inches into meter and centimeter.
feet = float(input("Enter distance in feet:"))
inches = float(input("Enter distance in inches:"))

total_inches = (feet * 12) + inches

centimeters = total_inches * 2.54

meters = int(centimeters // 100)
remaining_cm = centimeters % 100

print("Distance =", meters,"meters and",round(remaining_cm,2),"centimeters")