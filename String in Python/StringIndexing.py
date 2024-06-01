course="Python for Beginners"
# print(course[0])
print(course[0:2])  #Returns the whole string  characters from 0 index to 2 but excluding 2 i.e Here only 'Py'
print(course[0:])   #Returns the whole String characters from 0 index to last index means it assumes the last index
print(course[-1])   #Python assumes the negative indexes as a last characters of the string as comparing to other 
                                                                                           #programming languages 
print(course[:])   #Returns the whole whole string from index 0 upto last characters including last characters
another=print(course[:]) #Copy the whole string characters to another 
print(course[:2])

name="Jennifer"
print(name[1:-1])  #This prints the characters from index 1 upto ending chracters (-1) excluding end characters


