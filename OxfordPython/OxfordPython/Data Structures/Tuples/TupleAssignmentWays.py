"""
WAP to show the different ways of tuple assignments
"""

# an unnamed tuple of values assigned to values of another unnamed tuple
(val1,val2,val3) = (1,2,4)
print(val1,val2,val3)


Tup1 = (100,200,300)
(val1,val2,val3) = Tup1  # tuple assigned to another tuple
print(val1,val2,val3)

# expressions are evaluated before assignment
(val1,val2,val3) = (2+4, 5/3 + 4 , 9%3)
print(val1,val2,val3)

