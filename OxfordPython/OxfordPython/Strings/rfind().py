"""
Write a program that emulates the rfind function

The rfind() method finds the last occurrence of the specified value.

The rfind() method returns -1 if the value is not found.

The rfind() method is almost the same as the rindex() method.

programming tip: The start and end parameters in find() and rfind() are optional
"""

def rfind_ch(s,c):
    index = len(s) -1
    while index >=0:
        if s[index] == c:
            return index
        index = index -1
    return -1

str = input("Enter a string: ")

ch = input("Enter the character to be searched: ")

index = rfind_ch(str,ch)

if index != -1:
    print(ch,"is found at location",index)
else:
    print(ch,"is not present in the string")