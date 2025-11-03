#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

num_students = int(input("Enter the number of students:"))
all_percentages = []

for i in range(1, num_students+1):
    print(f"\n Enter marks of student {i}:")
    total = 0
    for j in range(1, 6):
        marks = float(input(f"Enter marks for subject {j}:"))
        total += marks

    percentage = total / 5
    all_percentages.append(percentage)
    print(f"Percentage of student {i}:{percentage:.2f}%")

average_percentage = sum(all_percentages) / num_students

print("\nAll students percentage:")
for i, p in enumerate(all_percentages, start = 1):
    print(f"student {i}:{p:.2f}%")

print(f"\nAverage Percentage of all students:{average_percentage:.2f}%")
        