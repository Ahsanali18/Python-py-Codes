# print(1/0)    #ValueError
# print(1+"1")  #typeError

try:
    number = int(input("Enter a number: "))
    print(f"{1/number:.2f}")
except ZeroDivisionError:
    print("You can't devide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong")
finally:
    print("Do some cleanup here!")