#Write a program to calculate the percentage of student based on marks of any 5 subjects.

m1 = int(input("Enter Marks of sunject1:"))
m2 = int(input("Enter Marks of sunject2:"))
m3 = int(input("Enter Marks of sunject3:"))
m4 = int(input("Enter Marks of sunject4:"))
m5 = int(input("Enter Marks of sunject5:"))

gain_marks = m1+m2+m3+m4+m5
percentage = (gain_marks / 500) * 100
print(f'Percentage is {percentage}%')
