from abc import ABC, abstractmethod
import math

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    
    def area(self):
        return float(f"{math.pi * self.radius**2:.2f}")

class Square(Shape):
    def __init__(self,side):
        self.side=side
    
    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping=topping
        
shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni",15)]

for shape in shapes:
    print(f"{shape.area()}cm²")