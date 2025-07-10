doubles = []

"""
for x in range(1,11):
    doubles.append(x * 2)

print(doubles)
"""
# List comprehension syntax:  doubles = [expression for value in iterable if condition]

# The above same code written in one-line
doubles = [x*2 for x in range(1,11)]
print(doubles)

triples = [y*3 for y in range(1,11)]
print(triples)

squares = [z**2 for z in range(1,11)]
print(squares)

fruits = ["apple","orange","banana","coconut"]
fruits = [fruit.upper() for fruit in fruits ]
print(fruits)

# 2nd way
# fruits = [fruit.upper() for fruit in ["apple","orange","banana","coconut"] ]
# print(fruits)

fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

# List of positive numbers from a mixed-numbers list
numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)

# List of negatibe numbers from a mixed-numbers list
negative_nums = [num for num in numbers if num < 0]
print(negative_nums)

# List of even numbers
even_nums = [ even_num for even_num in numbers if even_num%2 == 0 ]
print(even_nums)

odd_nums = [ odd_num for odd_num in numbers if odd_num%2  != 0 ]
print(odd_nums)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)