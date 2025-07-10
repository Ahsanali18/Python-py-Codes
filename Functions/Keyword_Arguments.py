def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title}{first_name} {last_name}")

# hello("Hello","Mr.","Ahsan","Ali")  # these are positional arguments here position/order matters.

hello("Hello",title="Mr.",last_name="Ali",first_name="Ahsan")   # these are keyword arguments here order doesn't matters.


for x in range(1,11):
    print(x, end=" ")  # here end is a keyword argument
print()

print("1","2","3","4","5",sep="-")  # here sep is a keyword argument

def get_phone(country_code, area_code, first_digits, last_digits):
    return f"{country_code}-{area_code}-{first_digits}-{last_digits}"

phone_num=get_phone(country_code=+92 ,area_code=311, first_digits=556, last_digits=334)
print(phone_num)