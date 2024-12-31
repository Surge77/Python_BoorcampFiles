"""
In a dictionary keys should be strictly of a type that is immutable.This means that a key can be of strings,number or
tuple type but it cannot be a list which is mutable.In case you try to make your key of a mutable type then a typeerror
will be generated
"""

Dict = {'Roll_No' : '16/001', 'Name' : 'Arav', 'Course' : 'Btech'}

print("Dict[Roll_No]",Dict['Roll_No'])
print("Dict[NAME]",Dict['Name'])
print("Dict[COURSE]",Dict['Course'])