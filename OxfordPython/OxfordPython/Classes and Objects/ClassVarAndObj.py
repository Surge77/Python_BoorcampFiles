"""
WAP to access class variable and object

Note:The python standard library is based on the concept of classes and objects.

In python everything is an object or instance of some class.Variables defined in a class are called class variables and
functions defined inside a class are called class methods.Class variables and class methods are together known as class
members.The class members can be accessed through class objects

Note: A class creates a new local namespace where all its attributes (data adn functions) are defined


"""

class ABC:
    var = 10

obj = ABC()

print(obj.var)

# the object of the class is created and used to access the class variable using the dot operator.Thus we can think of a
# class as a factory for making objects