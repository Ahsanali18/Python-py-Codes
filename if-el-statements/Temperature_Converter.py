temperatur=float(input("Enter the temperature: "))
unit = input("Is this temperatur in Celsius or Fahrenheit (C/F): ")

if unit == "C":
    temperatur = round((9*temperatur)/5 +32,1)
    print(f"The temperature in Fahrenheit is: {temperatur} ℉")
elif unit == "F":
    temperatur = round((temperatur-32) * 5/9,1)
    print(f"The temperature in Celsius is: {temperatur} ℃")
else:
    print(f"{unit} is an invalid unit of measurement.")