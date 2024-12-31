"""
WAP that uses docstrings and variable length arguments to add the values passed to function
"""

def add(*args):
    """Function returns the sum of values passed to it."""
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(add.__doc__)
print("Sum = ",add(25,45,23,45,12,34,78))