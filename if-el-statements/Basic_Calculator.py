operator=input("Enter an operator (+,-,*,/): ")

number1=float(input("Enter the 1st number: "))
number2=float(input("Enter the 2nd number: "))

if operator=="+":
    result=number1+number2
    print(round(result,3))

elif operator=="-":
    result=number1-number2
    print(round(result,3))

elif operator=="*":
    result=number1*number2
    print(round(result,3))

elif operator=="/":
    result=number1/number2
    print(round(result,3))

else:
    print(f"{operator} is not a valid operator!")