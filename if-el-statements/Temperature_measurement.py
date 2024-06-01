'''Write a python program in which take the value of temperature as an input from the user:
If temperature is greater than 30 degrees then prints the message 'Its a hot day' otherwise if it's less than 10
degrees then prints the message 'Its a cold day' otherwise print the message it's neither hot nor cold. '''

temperature=input("Enter the temperature of the day: ")
temperature=int(temperature)
if temperature>30:
    print("It's a hot day!")
elif temperature<10:
    print("It's a cold day!")
else:
    print("It's neither hot nor cold day!")
    