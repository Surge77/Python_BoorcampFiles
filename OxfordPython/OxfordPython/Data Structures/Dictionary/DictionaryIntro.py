"""
Dictionary is a data structure in which we store values as a pair of key and value.Each key is separated from its value
by a colon(:),and consecutive items are separated by comma.The entire items in a dictionary are enclosed in curly
brackets({})

To create a dictionary with one or more key-value pairs you can also use the dict() function.The dict() creates a
dictionary directly from a sequence of key value pairs.

WAP to create 10 key value pairs where key is a number in the range 1-10 and the value is twice the number

Keys must have unique values.Not even a single key can be duplicated in a dictionary.If you try to add a duplicate key,
then the last assignment is retained.
"""

Dict = {x: 2*x for x in range(1,10)}

print(Dict )

print(dict([('Roll_no','16/001'),('Name','Arav'),('Course','Btech')]))