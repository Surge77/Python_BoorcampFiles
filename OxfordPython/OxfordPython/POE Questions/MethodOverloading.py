"""
Define a base class called “shape” with a
method calculate_area. Create two objects as
triangle (take two parameters base &amp; height)
and square (takes only one parameter side
length) that use method from shape and
implement the calculate_area method
accordingly. (Hint: Method Overloading)
"""

class Shape:
    def calculate_area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

# Example usage:
triangle = Triangle(5, 10)
square = Square(4)
print("Triangle area:", triangle.calculate_area())
print("Square area:", square.calculate_area())

# using variable length arguments
class Shape:
    def calculate_area(self,*args):
        if len(args) == 0:
            print("Atleast enter one argument")
        elif len(args) == 1:
            print(f"The area of square is {args[0] * args[0]}")
        elif len(args) == 2:
            print(f"The area of triangle is {0.5 * args[0] * args[1]}")
        elif len(args) == 3:
            print(f"Too many arguments given")

square = Shape()
triangle = Shape()

square.calculate_area(5)
triangle.calculate_area(5,55)