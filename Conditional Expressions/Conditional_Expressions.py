number = 0
# result = "Positive" if number >0 else "Negative"

# result = "Even" if number%2 ==0 else "Odd"
# print(result)
a= 6
b= 7

max_number = a if a > b else b
min_number = a if a < b else b
print(f"Maximum number is: {max_number}")
print(f"Minimum number is: {min_number}")

age = 19
status= "Adult" if age >= 18 else "Child"
print(status)

temperature = 20
weather = "Hot" if temperature > 20 else "Cold"
print(weather)

user_role= "guest"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)
