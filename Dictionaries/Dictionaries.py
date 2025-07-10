capitals = {"USA": "Washington D.C.",
            "Pakistan":"Islamabad",
            "China":"Beijing",
            "Russia":"Moscow"}

# print(capitals)
# print(dir(capitals))
# print(capitals.get("Pakistan"))
# print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exists")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"}) #To update the existing value of the key present in the dictionary
capitals.pop("China")  # To remove the particular key-value pair from dictionary use pop() method
capitals.popitem()     # To remove the latest inserted key-value pair from dictionary use popitem() method 
# capitals.clear()
# print(capitals)

# keys = capitals.keys()    #returns the complete keys present in the dicitonary
# print(keys)

# for key in capitals.keys():
#     print(key)

# values = capitals.values()  #returns the complete values present in the dictionary
# print(values)

# for value in capitals.values(): 
#     print(value)

items = capitals.items()  #returns the complete key-value pairs
print(items)

for key,value in capitals.items():
    print(f"{key}: {value}")