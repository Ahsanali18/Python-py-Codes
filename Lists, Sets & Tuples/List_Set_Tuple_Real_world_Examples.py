shopping_cart = ["apple","banana","mango","milk"]
print(shopping_cart)
shopping_cart.append("bread")
print(shopping_cart)

daraz_shopping_cart = ["comb","t-shirt","glasses","shoes"]
print(daraz_shopping_cart)
daraz_shopping_cart.append("watch")
print(daraz_shopping_cart)

linkedIn_comments = ["Good Bro!","Nice work Bro!","Keep it up!","Awesome!"]
print(linkedIn_comments)
linkedIn_comments.append("MashaAllah!")
print(linkedIn_comments)


# Tuples use-cases
# Google Map Locatin of a particular place

location = (33.6844,73.0479)  #Islamabad
print(f"Islamabad Location: {location}")

# Screen Resolution
SCREE_RESOLUTION = (1920,1080)
print(f"SCREEN RESOLUTION: {SCREE_RESOLUTION}")

# Set use-cases
# Email system

registered_emails = {"ahsan@gmail.com","ahmed@gmail.com","zeeshan@gmail.com","nouman@gmail.com"}
if "ahmed@gmail.com" in registered_emails:
    print("This email is already taken!")

instagram_user_names = {"ahsan","ahsan0","ahsan1","ahsan10","ahsan11"}
new_user_name = input("Enter user-name: ")
if new_user_name in instagram_user_names:
    print("This user-name is already taken!")

frontend = {"HTML","CSS","JS"}
backend = {"Python","Django","JS"}


# Skills unique to front-end
print("Unique skills:",end=" ")
for skill in frontend:
    if skill in backend:
        continue
    print(skill,end=" ")

print()

# Skills common to both front-end and back-end
print("Common skills:",end=" ")
for skill in frontend:
    if skill in backend:
        print(skill, end=" ")

print()
# Method-2 Using difference of set and Union of set concept
unique_skills = frontend - backend
print("Unique skills:",*unique_skills)   #Note: * is an unpacking operator

common_skills = frontend & backend
print("Common skills:",*common_skills)