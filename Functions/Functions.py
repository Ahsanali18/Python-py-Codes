def happy_birthday(name,age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()

# happy_birthday("Ahsan",19)  #position of paratmeters matters 
# happy_birthday("Akbar",20)
# happy_birthday("Basit",21)


def display_invoice(user_name, amount, due_date):
    print(f"Hello {user_name}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Ahsan",42.50,"01/01")

# return statement

def add(x,y):
    z=x+y
    return z

def subtract(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def divide(x,y):
    z=x/y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

def create_name(first_name,last_name):
    first_name=first_name.capitalize()
    last_name=last_name.capitalize()
    return first_name +" "+ last_name

full_name=create_name("ahsan","ali")
print(full_name)