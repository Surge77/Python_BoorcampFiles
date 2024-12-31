"""
WAP to find the largest value in a list using reduce() function

reduce in Python from the functools module is a powerful tool for performing functional computations. This function
takes a predefined function and an iterable (like a list, tuple, or dictionary) and methodically applies the function
across the iterable to produce a single output value.

Unlike a traditional for loop, which requires explicit programming, reduce() simplifies this process, efficiently
 reducing the iterable to a single result—whether it be an integer, string, or boolean. This function, programmed in C,
offers optimized performance, making it an effective choice for data processing. By leveraging reduce(),
developers can execute complex computations with minimal code, ensuring both code efficiency and readability in Python
applications.
"""

import functools

def max_ele(x,y):
    return x>y

num_list = [4,1,8,2,9,3,0]

print("Largest value in the list is : ",functools.reduce(max,num_list))

