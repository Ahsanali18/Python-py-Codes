temperatur = 26
is_raining = True

# OR logical Operator
# if temperatur > 35 or temperatur < 0 or is_raining:
#     print("The outdoor event is canceled.")
# else:
#     print("The outdoor event is still scheduled.")


# and Logical Operator
is_sunny = False

if temperatur >=28 and is_sunny:
    print("It is Hot outside")
    print("It is Sunny!")
elif temperatur <=0 and is_sunny:
    print("It is Cold outside")
    print("It is Sunny!")
elif 28 > temperatur >0 and is_sunny:
    print("It is Warm outside")
    print("It is Sunny!")
elif temperatur >=28 and not is_sunny:
    print("It is Hot outside")
    print("It is Cloudy!")
elif temperatur <=0 and not is_sunny:
    print("It is Cold outside")
    print("It is Cloudy!")
elif 28 > temperatur >0 and not is_sunny:
    print("It is Warm outside")
    print("It is Cloudy!")

