"""
__del__() method

The init method which initializes when an object is created, the del method just works the opposite way.The __del__() method
is automatically called when an object is going out of scope.This is the time when an object will no longer be used
and its occupied resources are returned back to system

Tip: In java and c++ all members are private by default but in python they are public by default


"""

class ABC():
    class_var = 0   # class variable
    def __init__(self,var):
        ABC.class_var += 1
        self.var = var  # object variable
        print("The object value is : ",var)
        print("the value of the class variable is : ",ABC.class_var)

    def __del__(self):
        ABC.class_var -= 1
        print("Object with %d value is going out of scope"%self.var)

obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)

del obj1
del obj2
del obj3

