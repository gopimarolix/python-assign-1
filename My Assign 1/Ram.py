class Student:
    school = "freeCodeCamp.org"
    
    def __init__(self, name, course):
        self.name = name
        self.course = course
    
Student1 = Student("Gopi", "JavaScript")
Student2 = Student("sukumar", "Python")

print(Student1.name) 
print(Student2.name) 