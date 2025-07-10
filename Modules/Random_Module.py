import random

# print(help(random))

low = 1
high = 100

# random_number = random.randint(low,high)
random_number = random.random()  #gives the floating value between 0 - 1
print(random_number)

options = ("rock","paper","scissors")
option = random.choice(options)
print(option)

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)