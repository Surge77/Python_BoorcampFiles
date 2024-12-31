"""
Program to illustrate the use of a private method

syntax: objectname._classname__privatemethodname
to access the private method in class
"""

class ABC():
    def __init__(self,var):
        self.__var = var
    def __display(self):
        print("From class method, var  = ",self.__var)

obj = ABC(10)

obj._ABC__display()