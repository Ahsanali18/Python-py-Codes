def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is Tuesday"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thursday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _: #default case 
            return "Not a valid day!"

print(day_of_week(1))
print(day_of_week("Pizza"))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":   # | is or operator 
            return True
        case _:
            return False

print(is_weekend("Sunday"))
print(is_weekend("Pizza"))

