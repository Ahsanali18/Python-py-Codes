import math

class Shape:
    def __init__(self, color, is_filled):
        self.color=color
        self.is_filled=is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'Filled' if self.is_filled else 'Not Filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color,is_filled)
        self.radius=radius
    # Method overriding is performed here and the circle can obviously invokes it's own describe() method rather than it's parent
    def describe(self):
        print(f"It is a circle with an area of {math.pi * self.radius**2:.2f}cm²")
        super().describe() # to invoke the describe() method of parent also use super() method
    
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color,is_filled)
        self.width=width
    
    def describe(self):
        print(f"It is a square with an area of {self.width**2:.2f}cm²")
        super().describe() # to invoke the describe() method of parent also use super() method
    
class Triagnle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color,is_filled)
        self.width=width
        self.height=height
    
    def describe(self):
        print(f"It is a triangle with an area of {self.width* self.height/2:.2f}cm²")
        super().describe() # to invoke the describe() method of parent also use super() method
    


circle = Circle(color="Red",is_filled=True,radius=5)
print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")
circle.describe()

square = Square(color="Blue", is_filled=False,width=6)
print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
square.describe()

triangle = Triagnle(color="Yellow", is_filled=True,width=7, height=8)
print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")
triangle.describe()