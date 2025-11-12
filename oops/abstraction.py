# hidding unnecesary details from user through class, methods

class Student:
    def __init__(self,name,grade,percentage):  # Methods
        self.name = name #attribute
        self.grade = grade #attribute
        self.percentage = percentage #attribute
        
    
    def Student_details(self): # Method abstraction
        print(f"{self.name} is in class {self.grade} with {self.percentage+2}%") #hidden from user(who is calling this method)


#Object - instance of clss
Student1 = Student("Sunil",11,10)
Student2 = Student("Anil",12,30)

Student1.Student_details()
