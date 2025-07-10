"""
name = input("Enter your name: ")
while name == "":
    print("You didn't entered your name")
    name = input("Enter your name: ")

print(f"Hello {name}")


age = int(input("Entre your age: "))

while age<0:
    print("Age can't be negative")
    age=int(input("Enter your age: "))

print(f"You are {age} years old")

food = input("Enter a food you like (q/Q to quit): ")

while not food.lower() == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q/Q to quit): ")

print("Bye Bye!")
"""

number = int(input("Enter a # between 1 - 10: "))

while number < 1 or number > 10:
    print(f"{number} is not valid")
    number = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {number}.")