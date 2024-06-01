course="Python for Beginners"
print(len(course))   #This len() is used whenever we are taking the input from user (It's general purpose function)

print(course.upper()) #Creates new string of Upper case 
print(course) #Our Original course variable not modified by upper()

print(course.lower()) #Creates new string of Lower case
print(course) #Our Original course variable not modified by lower()

print(course.find('Beginners'))  #Finds the characters in the string and returns their index (Case sensitive)

print(course.replace("Beginners", "Absolute Beginners")) #Replaces the first string characters to another string characters
print(course)

                                # in operator (Returns True or False)

print('Python' in course)   #Here we are checking that Python is in the course variable and if yes then it returns
                            #True  
print('----' in course)  #Here it checks that ---- are present in course string vatriable if yes then it returns 
                                                    #True otherwise it returns False
                                                    