"""
zip() is a built-in function that takes two or more sequences and "zips" them into a list of tuples.The tuple this ,
formed has one element from each sequence.

Program to show the use of zip() function
"""

tup = (1,2,3,4,5)

list1 = ['a','b','c','d','e']

print(list(zip(tup,list1)))