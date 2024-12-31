"""
WAP to demonstrate slice operation on string objects
"""

str = "PYTHON"

print("str[1:5] = ", str[1:5]) # characters starting at index 1 and extending up to but but not including 5
print("str[:6] = ", str[:6]) # defaults to the start of the string
print("str[1:] = ", str[1:]) # defaults to the end of the string
print("str[:] = ", str[:]) # defaults to the entire string
print("str[0:20] = ", str[0:20]) # an index that is too big is truncated down to length of string