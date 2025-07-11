class Student:

    class_year = 2024  #class variable
    num_of_students = 0  # class variable to count the number of students (keep track of amount of students)

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_of_students+=1   # Here we incrementing the class variable to count the number of students as student objects are created

student1 = Student("Ahsan",19)
student2 = Student("Ahmed",20)        

print(student1.name)
print(student1.age)
print(Student.class_year)   # It's prefer to call the class variable using the class name directly 

print(student2.name)
print(student2.age)
print(Student.class_year)   # It's prefer to call the class variable using the class name directly 

print(Student.num_of_students)   #Number of students after creating two students objects (student1,student2)


student3 = Student("Sachin",20)
student4 = Student("Zeeshan",20)
print(Student.num_of_students)   #Number of students after creating four students objects (student1,student2,student3,student4)

print(f"My graduating class of {Student.class_year} has {Student.num_of_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)