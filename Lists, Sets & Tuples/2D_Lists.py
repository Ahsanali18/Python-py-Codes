# fruits =     ["apple","orange","banana","coconut"]
# vegetables = ["celery","carrots","potatoes"]
# meats =      ["chicken","fish","turkey"]

# groceries= [fruits,vegetables,meats]

# fruits[0]="pineapple"
# print(fruits)

# print(groceries[0])     #complete fruits list
# print(groceries[0][0])  #first fruit in fruits list


# Is same as the above code
# groceries = [["apple","orange","banana","coconut"],
#              ["celery","carrots","potatoes"],
#              ["chicken","fish","turkey"]]


# # for collection in groceries:
# #     print(collection)

# for collection in groceries:
#     for food in collection:
#         print(food,end=" ")
#     print()

# Tuples
"""g
roceries = [("apple","orange","banana","coconut"),
             ("celery","carrots","potatoes"),
             ("chicken","fish","turkey")]

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()
"""

groceries = [{"apple","orange","banana","coconut"},
             {"celery","carrots","potatoes"},
             {"chicken","fish","turkey"}]

for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()
