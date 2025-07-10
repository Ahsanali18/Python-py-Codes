fruits = ["apple","orange","banana","coconut"]

# print(fruits[::2]) # every second fruit
# print(fruits[::-1])

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))

# print("apple" in fruits)   # returns True or False if fruit is present
# print("pineaple" in fruits)


# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("coconut"))
# print(fruits.count("banana"))
# print(fruits)
# for fruit in fruits:
#     print(fruit)

#set : unordered values
# fruits = {"apple","orange","banana","coconut","coconut"}
# print(dir(fruits))
# print("apple" in fruits)

# print(fruits[0]) # shows an error because set is an unordered

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()
# print(fruits)

# tuple (): ordered and unchangeable

fruits = ("apple","orange","banana","coconut","coconut")
print(fruits)
# print(help(fruits))
print(dir(fruits))

print(fruits.count("coconut"))
print(fruits.index("apple"))
print(len(fruits))
