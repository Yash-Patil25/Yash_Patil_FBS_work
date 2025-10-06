#Write a program to convert days into years, weeks and days.

days = int(input("enter number of days:"))

years = days // 365
weeks = (days % 365) // 7
remaining_days = (days % 365) % 7

print("Years:",years)
print("Weeks:",weeks)
print("Remaining days:",remaining_days)

