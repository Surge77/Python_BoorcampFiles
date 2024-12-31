"""
Class methods are defined in the class.Class methods must have the first argument named as self.The self argument refers
to the object itself.That is the object that has called the method.This means that even if a method that takes no
arguments,it should be defined to accept the self.

WAP to access class members using the class object

Key points to remember:
-The statements inside the class definition must be properly indented
-Class that has no other statements should have a pass statement at least
-Class methods or functions that begin with double underscore(__) are special functions with a predefined and special
meaning
"""

class ABC:
    var = 10
    def display(self):
        print("In class method....")


obj = ABC()

print(obj.var)
obj.display()