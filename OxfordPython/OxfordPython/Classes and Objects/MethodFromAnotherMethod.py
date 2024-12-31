"""
Program to call a class method from another method of the same class

To remember: Like functions and modules class also has a documentation string which can be accessed using
className.__doc__.
"""

class ABC():
    def __init__(self,var):
        self.var = var
    def display(self):
        print("Var is : ",self.var)
    def add_2(self):
        self.var += 2
        self.display()

obj = ABC(10)
obj.add_2()