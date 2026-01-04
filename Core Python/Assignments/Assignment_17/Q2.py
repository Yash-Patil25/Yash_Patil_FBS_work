# Create a derived class from Student as EnggStudent with :
#a. Data members as :
#i. Branch
#ii. InternalMarks

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

# class EnggStudent(Student):
#     def __init__(self, student_id, name, age, percentage, branch, internal_marks):
#         super().__init__(student_id, name, age, percentage)
#         self.Branch = branch
#         self.InternalMarks = internal_marks

#     def Accept(self):
#         super().Accept()
#         self.Branch = input("Enter Branch: ")
#         self.InternalMarks = int(input("Enter Internal Marks: "))

#     def __str__(self):
#         return (super().__str__() +
#                 f"\nBranch: {self.Branch}"
#                 f"\nInternal Marks: {self.InternalMarks}")

# if __name__ == "__main__":
#     e1 = EnggStudent(0, "", 0, 0.0, "", 0)
#     e1.Accept()
#     e1.CalculateRank()
#     print(e1)


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

class EnggStudent(Student):

    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        super().__init__(student_id, name, age, percentage)
        self.Branch = branch
        self.InternalMarks = internal_marks

    def Accept(self):
        super().Accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = int(input("Enter Internal Marks: "))

    def CalculateRank(self):
        if self.Percentage >= 85 and self.InternalMarks >= 40:
            self.Rank = "Distinction"
        elif self.Percentage >= 70 and self.InternalMarks >= 35:
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
        return (super().__str__() +
                f"\nBranch: {self.Branch}"
                f"\nInternal Marks: {self.InternalMarks}")

if __name__ == "__main__":
    e1 = EnggStudent(0, "", 0, 0.0, "", 0)
    e1.Accept()
    e1.CalculateRank()
    e1.Display()

