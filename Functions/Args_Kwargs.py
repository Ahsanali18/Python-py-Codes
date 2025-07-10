def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()

    # if there is apartment key present in our kwargs dictionary then print it's value rather than none if it's not
    if "apartment" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apartment')}")
    else: # if the person doesn't have apartment then just simply print it's street
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip_code')}")

shipping_label("Engr.","Ahsan","Ali","Memon",
               street="Al-Rehman City",
               apartment="101",
               city="Hyderabad",
               state="Sindh",
               zip_code="8238",
               country="Pakistan")