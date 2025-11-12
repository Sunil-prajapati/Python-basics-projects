# class - blueprint or template
class Student:
    def __init__(self,name,grade,percentage):  # Methods
        self.name = name #attribute
        self.grade = grade #attribute
        self.percentage = percentage #attribute
        
    
    def Student_details(self): # Method
        print(f"{self.name} is in class {self.grade} with {self.percentage}")


#Object - instance of clss
Student1 = Student("Sunil",11,80)
# print(Student1.name, Student1.grade)
# Student1.Student_details()
print(Student1.__dict__)

Student2 = Student("Vishaka",10,30)
# print(Student2.name, Student2.grade)


# MOdify object property 
Student1.percentage = 33
print(Student1.percentage)

#del 
del Student1.percentage