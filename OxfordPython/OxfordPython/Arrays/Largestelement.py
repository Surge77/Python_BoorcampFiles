"""
Program to find the largest element in array
"""


import array


arr = array.array('i',[1,2,3,56,12,43,89,65,78,98,4,5,6])

greatest = 0

for i in arr:
    if i>greatest:
        greatest = i
    else:
        pass

print(greatest)