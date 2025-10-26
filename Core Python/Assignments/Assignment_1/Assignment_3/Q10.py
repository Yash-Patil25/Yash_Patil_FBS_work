#Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender = input("Enter (male/female):").lower()
age = int(input("Enter Age:"))

if gender == "male":
    if age >= 21:
        print("You are eligible to marry.")
    else:
        print("You are not eligible to marry.")
elif gender == "female":
    if age >= 18:
        print("You are eligible to marry.")
    else:
        print("You are not eligible to marry.")
else:
    print("Invalid gender entered.")