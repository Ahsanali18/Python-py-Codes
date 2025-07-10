name = input("Enter your full name: ")

print(len(name))       # returns the amount of total number of characters present in the string literal
print(name.find("a"))  # returns the first occurence of a given character
print(name.rfind("A")) # returns the last  occurence of a given character

title = "hey, This is about to good! Tell me something about you?"
print(title.capitalize()) #capitalize the first character of the string literal
print(name.upper())       #capitalize all the  characters of the string literal
print(name.lower())       #makes all the characters in a lower case
print(name.isdigit())     #checks the string only contains the digit then returns True otherwise False
print(name.isalpha())     #checks the string only contains the alphabets then returns True otherwise False

cnic_number = input("Enter your CNIC number: ")
print(cnic_number.count("-"))
cnic_number = cnic_number.replace("-","") # replaces the particular character with the given character here dashes with empty string
print(cnic_number)

print(help(str))  # returns the complete information about the strings. The number of methods it has all the information.
