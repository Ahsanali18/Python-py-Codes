# Validate user input exercise:
# 1. username is no more than 12 characters.
# 2. username must not contain spaces
# 3. username must not contains digits.

user_name = input("Enter username: ")

if len(user_name) > 12 and user_name:
    print("Your username can't be more than 12 characters.")

elif not user_name.find(" ") == -1:
    print("Your username can't contains spaces")

elif not user_name.isalpha():
    print("Your username can't contains numbers")

else:
    print(f"Welcome {user_name}")