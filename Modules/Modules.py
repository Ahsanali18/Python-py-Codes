# print(help("modules")) # to display the list of python-built in modules

# import math            # simple way to import the module
# import math as m       # another way to import the module using as an alias
# from math import pi    # another way to import the particular function from the module

# print(f"{m.pi:.2f}")

import ExampleModule 

print(help(ExampleModule))

result = ExampleModule.pi
print(result)

square_result = ExampleModule.square(3)
print(square_result)

cube_result = ExampleModule.cube(4)
print(cube_result)

cicumference = ExampleModule.cicumference(2)
print(cicumference)