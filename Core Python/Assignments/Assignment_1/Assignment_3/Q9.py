#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1 = float(input("Enter sub1 marks:"))
sub2 = float(input("Enter sub2 marks:"))
sub3 = float(input("Enter sub3 marks:"))
sub4 = float(input("Enter sub4 marks:"))
sub5 = float(input("Enter sub5 marks:"))

total = sub1+sub2+sub3+sub4+sub5
percentage = total / 5

print("Total Marks:", total)
print("Percentage:",percentage,"%")
if percentage >= 75:
    print("Grade: Distinction")
elif percentage >= 60:
    print("Grade: First class")
elif percentage >= 50:
    print("Grade: second class")
elif percentage >= 40:
    print("Grade: pass class")
else:
    print("Grade: fail")