from math import pi as PI
# Enhance your understanding of polymorphism in Python by creating a set of classes that demonstrate method overriding and polymorphic behavior.

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must override area()")



class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius

    def area(self):
        return PI * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length: float, width:float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

