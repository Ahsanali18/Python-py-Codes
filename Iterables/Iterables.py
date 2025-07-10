numbers = [1,2,3,4,5]

"""
for number in numbers:
    print(number,end=" ")

print()

for number in reversed(numbers):
    print(number, end=" ")
"""

"""
fruits = {"apple","orange","banana","coconut"}
for fruit in fruits:  #note we can apply reversed() method on sets because they can't be reversed
    print(fruit)
"""

name = "Ahsan Ali"
for character in name:
    print(character,end=" ")


my_dictionary = {"A":1,
                 "B":2,
                 "C":3,
                 "D":4,
                 "E":5}

for key, value in my_dictionary.items():
    print(f"{key:2}= {value}")
