from Script1 import *

# Output : Nothing should be printed if there is if and main statements are present if we remove them then the whole output will be printed.

def favourite_drink(drink):
    print(f"Your favourtite drink is {drink}")

def main():
    print("This is script2")
    favourtite_food("Burger")
    favourite_drink("Milk")
    print("Good Bye!")

if __name__ == '__main__':
    main()