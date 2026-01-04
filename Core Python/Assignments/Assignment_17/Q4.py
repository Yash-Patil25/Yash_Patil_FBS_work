#4. Create a class College which has collection of students. Add the
#following methods :
#a. Parameteried constructor for number of students.
#b. AddStudent
#c. GetStudent
#d. RemoveStudent
#e. Override __str__ Method

class College:
    def __init__(self, capacity):
        self.capacity = capacity
        self.students = []

    def AddStudent(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            print("Student added successfully")
        else:
            print("College capacity full")

    def GetStudent(self, student_id):
        for student in self.students:
            if student.StudentId == student_id:
                return student
        return "Student not found"

    def RemoveStudent(self, student_id):
        for student in self.students:
            if student.StudentId == student_id:
                self.students.remove(student)
                print("Student removed successfully")
                return
        print("Student not found")

    def __str__(self):
        result = f"\nCollege Capacity: {self.capacity}\nStudents List:"
        for student in self.students:
            result += "\n" + str(student)
        return result

class Student:
    def __init__(self, student_id, name):
        self.StudentId = student_id
        self.Name = name

    def __str__(self):
        return f"Student ID: {self.StudentId}, Name: {self.Name}"

if __name__ == "__main__":
    c1 = College(2)

    s1 = Student(101, "Yash")
    s2 = Student(102, "Amit")

    c1.AddStudent(s1)
    c1.AddStudent(s2)

    print(c1)

    print("\nGet Student:", c1.GetStudent(101))

    c1.RemoveStudent(101)
    print(c1)
