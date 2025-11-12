class Student:
    def __init__(self,name,grade,percentage):  # Methods
        self.name = name 
        self.grade = grade 
        self.percentage = percentage
        
    def Student_details(self): # Method
        print(f"{self.name} is in class {self.grade} with {self.percentage}")

Student1 = Student("Sunil",11,80)


class GraduateStudent(Student):
    def __init__(self,name,grade,percentage,stream):
        super().__init__(name,grade,percentage)
        self.stream = stream
        
    def Student_details(self): # method inheritance
       super().Student_details() # in polymorphism we don't use super in method and method name is same as parent
       print(f"Stream is {self.stream}")


GraduateStudent1 = GraduateStudent("someone",10,33,"Non-Medical")
print(GraduateStudent1.Student_details())
        