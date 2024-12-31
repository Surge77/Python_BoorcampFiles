"""
WAP using map() function to create a list of squares of numbers in the range 1-10
"""

def sqr(x):
    return x*x

sq_list = list(map(sqr,range(1,11)))

print("list of squares from 1-10: ",sq_list)