#Write a program to check if entered year is a leap year or not.

def is_leap(year):
    if(year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

year = int(input("Enter a year:"))

if is_leap(year):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")