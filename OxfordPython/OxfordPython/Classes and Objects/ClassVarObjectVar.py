"""
We know class has variables defined in it.These variables are of two types: class variables and object variables.
As the name suggests class variables are owned by the class and object variables are owned by each object.

-If a class has n objects,then there will be n separate copies of the object variable as each object will have its own
object variable
-the object variable in not shared between objects
-A change made to the object variable by one object will not be reflected in other objects

-If a class has one class variable,then there will be one copy only for that variable.All the objects of that class will
share the class variable
-Since there exists a single copy of the class variable,any changes made to the class variable by an object will be
reflected in all other objects

Note:Class variables and object variables are ordinary variables that are bound to the class's and object's namespace
respectively

Note: Class variables are usually used to keep a count of number of objects created from a class

Program to differentiate between class and object variable
"""

class ABC:
    class_var = 0   # class variable
    def __init__(self,var):  # here self means the object itself is passed as a first parameter in the method
        ABC.class_var += 1
        self.var = var # object variable
        print("The object values is : ",var)
        print("The value of class variable is : ",ABC.class_var)

obj1 = ABC(10)
obj2 = ABC(20)
obj3 = ABC(30)

"""
We have a class_Var which is shared by all three objects of the class.It is initialized to zero and each times an object
is created,the class_var is incremented by 1.Since the variable is shared by all objects.Changes made to class_var by one
object is reflected in other objects as well'

Then we have object variable which is unique for every object.When an object is created and the __init__() method is 
called,the object variable is initialized.The object variable belongs to only a particular object
"""