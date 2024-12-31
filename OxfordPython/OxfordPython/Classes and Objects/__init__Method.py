"""
The __init__() method has a special significance.The __init__() method is automatically executed when object of a class
is created.

Note:The __init__() method is same as constructor in c++ and java

Program to illustrate the use of __init__() method

Note that we have created an object in the main module and no where we have called the __init__() method.This is
because the __init__() method is automatically involved when the object of class is created

Note: it is a good habit to initialize all attributes in the __init__() method.Although values can be initialized in
other methods also but is not recommended
"""

class ABC:
    def __init__(self,val):
        print("In class method...")
        self.val = val
        print("the val is: ",val)

obj = ABC(10)