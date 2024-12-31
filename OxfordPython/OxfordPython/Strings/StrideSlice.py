"""
WAP to use slice operation with stride

In the slice operation you can specify a third argument as the stride,which refers to the number of characters to move
forward after the first character is retrieved from the string.The default value of stride is 1.Hence in all the above
examples where the values of stride is not specified,its default value is 1 is used which means that every character
between two index numbers is retrieved.

Note:even whitespace characters are skipped as they are part of the string
"""

str = "Welcome to the world of python"

print("str[2:10] = ", str[2:10]) # default stride is 1
print("str[2:10:1] = ", str[2:10:1]) # same stride = 1
print("str[2:10:2] = ", str[2:10:2]) # skips every alternate character
print("str[2:13:4] = ", str[2:13:4]) # skips every fourth character
