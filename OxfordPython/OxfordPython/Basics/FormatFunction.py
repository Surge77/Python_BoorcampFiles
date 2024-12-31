print(format(3.45644,'.2f'))

# it is always recommended to use the built in format() function to produce a string version of a number with a specific
# number of decimal places.

a = format(3**50,'.5e')
print(a)
# The format function can also be used to format floating point number in scientific notation
"""
The result is formatted in scientific notation with five decimial places of precision.this feature is especially useful
when displaying results in which only certain number of decimal places is needed
"""

print(format(123455,','))

# Note: there is no char data type in python