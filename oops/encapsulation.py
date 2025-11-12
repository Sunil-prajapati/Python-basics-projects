#Restrict access to certain attributes or methods to prtect data
class Student:
    def __init__(self,name,grade,percentage):  # Methods
        self.name = name 
        self.grade = grade 
        self.__percentage = percentage  #double underscore limits access (make it private)
        
    def get_percentage(self):  # Encapsulation
        return self.__percentage
    
    def Student_details(self): # Method 
        print(f"{self.name} is in class {self.grade} with {self.percentage+2}%")


#Object - instance of clss
Student1 = Student("Sunil",11,10)
Student2 = Student("Anil",12,30)

print(Student1.get_percentage())