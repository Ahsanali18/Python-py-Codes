# Membership Operators: in, not in
"""
word = "APPLE"
letter =  input("Guess a letter in the secret word: ").upper()
# 1st way to check

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found!")

# 2nd way to check (Opposite to the above ones)
if letter not in word:
    print(f"{letter} was not found!")
else:
    print(f"There is a {letter}")
"""

# Set of students
"""
students = {"Ahsan","Ahmed","Sameer"}
student = input("Enter the name of a student: ")
if student in students:
    print(f"{student} is student!")
else:
    print(f"{student} was not found!")
"""

"""
grades = {"Ahsan":"A",
          "Ahmed":"B",
          "Sachin":"A",
          "Sameer":"C",
          "Akbar":"D"}

student = input("Enter the name of a student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found!")
"""

# Real world example: (Real use-case of in and not in operators)
email_address = "ahsanali@gmail.com"
if "@" in email_address and "." in email_address:
    print(f"{email_address} is a valid email.")
else:
    print(f"{email_address} is an invalid email.")