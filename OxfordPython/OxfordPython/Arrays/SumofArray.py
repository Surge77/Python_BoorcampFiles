"""
Program to find the sum of arrays

"""

import array

arr = array.array('i',[1,3,4,5,3])


sum = 0

for i in arr:
    sum += i

print(sum)