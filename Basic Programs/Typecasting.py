name = "Ahsan Ali"
age = 19
gpa = 3.75
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa) #typecasting the gpa floating variable into an integer.
print(gpa)

# age= str(age)

# age+=1    # shows an error
# age+="1"  # works well without any error
# print(age)

name= bool(name)
print(name)
