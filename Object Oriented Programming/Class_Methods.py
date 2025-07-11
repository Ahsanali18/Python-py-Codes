class Student:
    # Class variables
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count+=1 
        Student.total_gpa+=gpa
    
    # INSTANCE METHOD
    def get_info(self):  #This is an instance method and they have self as a first parameter
        return f"{self.name} {self.gpa}"
    
    @classmethod 
    def get_count(cls):  #This is a class method and they have cls (class) as a first attribute parameter
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count:.2f}"


print(Student.get_count())  # prints Total number of students: 0

student1 = Student("Ahsan",3.76)
student2 = Student("Sachin",3.78)
student3 = Student("Basit",3.81)

print(Student.get_count())
print(Student.get_average_gpa())
