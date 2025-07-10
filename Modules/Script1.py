# print(__name__)  # prints the __main__

# from Script2 import *
# print(__name__) 
# output:
# Script2  (from script2 print statement)
# __main__ (from the current script1 file)

def favourtite_food(food):
    print(f"Your favourtite food is {food}")


def main():
    print("This is script1")
    favourtite_food("Shawarma")
    print("Good Bye!")

if __name__ == '__main__':
    main()

# print("This is script1")
# favourtite_food("Shawarma")
# print("Good Bye!")
