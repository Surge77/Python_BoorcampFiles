"""
WAP that uses enumerate() function to print elements as well as their indices

The enumerate() function in Python is a built-in function that takes a sequence (such as a list, tuple, or string) as an
argument and returns an enumerate object. This object can be iterated over to produce pairs of values: the index of the
current item in the sequence, and the item itself.

"""

for index,element in enumerate('ABCDEFGH'):
    print(index,element)