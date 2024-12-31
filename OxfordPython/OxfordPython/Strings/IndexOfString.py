"""
Program to demonstrate an expression used an index of a string

Also note that even the whitespaces characters,exclamation mark and any other symbol that forms a part of the string
would be assigned its own index numbers
"""

str = "Hello, welcome to the world of python"

i = 2

print(str[i]) # index is an integer
print(str[i*3+1])  # index is an expression that evaluates to an integer

