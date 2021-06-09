class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def get_grade(self):
        return self.grade

class Course():
    def __init__(self,subject,max_students):
        self.subject = subject
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()
            return total/(len(self.students))

s1=Student(name="Sarah",grade=100)
s2=Student(name="Kelvin",grade=98)

course=Course("English",2)
course.add_student(s2)
course.add_student(s1)