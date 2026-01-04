#1. Create a class Student with following
#a. data members :
#i. StudentId
#ii. Name
#iii. Age
#iv. Percentage

# class Student:
#     def __init__(self,student_id=0,name="Not Assigned",age=0,percentage=0.0):
#         self.StudentId = student_id
#         self.Name = name
#         self.Age = age
#         self.Percentage = percentage

#     def ShowStudent(self):
#         print("\nStudent ID:",self.StudentId)
#         print("Name:",self.Name)
#         print("Age:",self.Age)
#         print("Percentage:",self.Percentage)

# if __name__ == "__main__":
#     s1 = Student()
#     s2 = Student(101,"Yash Patil",21,82.5)

#     s1.ShowStudent()
#     s2.ShowStudent()



#b.Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. Method CalculateRank
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

if __name__ == "__main__":
    s1 = Student(0, "", 0, 0.0)
    s1.Accept()
    s1.CalculateRank()
    s1.Display()
