#3 a. Create a class MedicalStudent inherited from Student with following:
#i. Data members :Specialization
#ii. MarksOfInternship

# class Student:
#     def __init__(self, student_id, name, age, percentage):
#         self.StudentId = student_id
#         self.Name = name
#         self.Age = age
#         self.Percentage = percentage
#         self.Rank = ""

#     def Accept(self):
#         self.StudentId = int(input("Enter Student ID: "))
#         self.Name = input("Enter Name: ")
#         self.Age = int(input("Enter Age: "))
#         self.Percentage = float(input("Enter Percentage: "))

#     def CalculateRank(self):
#         if self.Percentage >= 85:
#             self.Rank = "Distinction"
#         elif self.Percentage >= 70:
#             self.Rank = "First Class"
#         elif self.Percentage >= 60:
#             self.Rank = "Second Class"
#         elif self.Percentage >= 40:
#             self.Rank = "Pass"
#         else:
#             self.Rank = "Fail"

#     def __str__(self):
#         return (f"\nStudent ID: {self.StudentId}"
#                 f"\nName: {self.Name}"
#                 f"\nAge: {self.Age}"
#                 f"\nPercentage: {self.Percentage}"
#                 f"\nRank: {self.Rank}")

# class MedicalStudent(Student):

#     def __init__(self, student_id, name, age, percentage,
#                  specialization, marks_of_internship):
#         super().__init__(student_id, name, age, percentage)
#         self.Specialization = specialization
#         self.MarksOfInternship = marks_of_internship

#     def Accept(self):
#         super().Accept()
#         self.Specialization = input("Enter Specialization: ")
#         self.MarksOfInternship = int(input("Enter Internship Marks: "))

#     def CalculateRank(self):
#         if self.Percentage >= 80 and self.MarksOfInternship >= 60:
#             self.Rank = "Excellent"
#         elif self.Percentage >= 65:
#             self.Rank = "Good"
#         elif self.Percentage >= 50:
#             self.Rank = "Average"
#         else:
#             self.Rank = "Needs Improvement"

#     def Display(self):
#         print(self)

#     def __str__(self):
#         return (super().__str__() +
#                 f"\nSpecialization: {self.Specialization}"
#                 f"\nInternship Marks: {self.MarksOfInternship}")

# if __name__ == "__main__":
#     m1 = MedicalStudent(0, "", 0, 0.0, "", 0)
#     m1.Accept()
#     m1.CalculateRank()
#     m1.Display()


#b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. override Method CalculateRank
#v. Override __str__ Method

class Student:
    def __init__(self, student_id, name, age, percentage):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage
        self.Rank = ""

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def CalculateRank(self):
        if self.Percentage >= 85:
            self.Rank = "Distinction"
        elif self.Percentage >= 70:
            self.Rank = "First Class"
        elif self.Percentage >= 60:
            self.Rank = "Second Class"
        elif self.Percentage >= 40:
            self.Rank = "Pass"
        else:
            self.Rank = "Fail"

    def Display(self):
        print(self)

    def __str__(self):
        return (f"\nStudent ID: {self.StudentId}"
                f"\nName: {self.Name}"
                f"\nAge: {self.Age}"
                f"\nPercentage: {self.Percentage}"
                f"\nRank: {self.Rank}")

class MedicalStudent(Student):

    def __init__(self, student_id, name, age, percentage,
                 specialization, marks_of_internship):
        super().__init__(student_id, name, age, percentage)
        self.Specialization = specialization
        self.MarksOfInternship = marks_of_internship

    def Accept(self):
        super().Accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = int(input("Enter Internship Marks: "))

    def CalculateRank(self):
        if self.Percentage >= 80 and self.MarksOfInternship >= 60:
            self.Rank = "Excellent"
        elif self.Percentage >= 65:
            self.Rank = "Very Good"
        elif self.Percentage >= 50:
            self.Rank = "Good"
        else:
            self.Rank = "Fail"

    def Display(self):
        print(self)

    def __str__(self):
        return (super().__str__() +
                f"\nSpecialization: {self.Specialization}"
                f"\nInternship Marks: {self.MarksOfInternship}")

if __name__ == "__main__":
    m1 = MedicalStudent(0, "", 0, 0.0, "", 0)
    m1.Accept()
    m1.CalculateRank()
    m1.Display()

