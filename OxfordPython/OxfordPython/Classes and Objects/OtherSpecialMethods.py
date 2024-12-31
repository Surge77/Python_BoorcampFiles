"""
The use of other special methods

__repr__() : This method has built-in function with syntax repr(object).It returns a string representation of an object.
                The function works on any object,not just class instances

__cmp__():This method is called to compare two class objects.In fact,the function can even compare any two python
            objects by using the equality operator(==)For class instances the cmp method can be defined to write the
            customized comparison logic

__len__():This method function has built in function that has the syntax len(objects) It returns the length of an
            object
"""

class ABC():
    def __init__(self,name,var):
        self.name = name
        self.var = var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self, other):
        return self.var - other.var

obj = ABC("abcdef",10)

print("The value stored in object is: ",repr(obj))
print("The length of the name stores in object is: ",len(obj))
obj1 = ABC("ghijkl",1)

val = obj.__cmp__(obj1)

if val == 0:
    print("Both have equal values")
elif (val == -1 ):
    print("First value is less than second")
else:
    print("Second value is less than first")