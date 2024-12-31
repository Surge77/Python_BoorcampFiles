"""
WAP to understand how characters in a string are accessed using negative indices
"""

str = "PYTHON"

print("str[-1] = ", str[-1])  # last character is accessed

print("str[-6] = ", str[-6])  # first character is accessed
print("str[-2:] = ", str[-2:])  # second last and last characters are accessed
print("str[:-2] = ", str[:-2])  # all characters up-to but not including second last
print("str[-5:-2] = ", str[-5:-2])  # characters from second up-to second last are