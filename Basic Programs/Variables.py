# Strings
first_name = "Ahsan"  # variable-1
food = "Shawarma"
email = "a123@gmail.com"

print(first_name)
# print("first_name")

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

# Integers
age = 19
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# Float
price = 10.99
gpa = 3.75
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km")

# Boolean
is_student = True
for_sale = True
is_online = True

print(f"Are you a student?: {is_student}")
print(f"That item is for sale: {for_sale}")

if is_student:
    print("You are student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

if is_online:
    print("You are online")
else:
    print("You are offline")