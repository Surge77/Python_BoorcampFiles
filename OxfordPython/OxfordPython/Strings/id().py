"""
WAP to demonstrate string references using the id function

Python strings are immutable which means once that once created they cannot be changed.Whenever you try to modify an
existing string variable a new string is created

Every object in python is stored in memory.You can find out whether two variables are referring to the same object or
not by using the id().The id function returns the memory address of that object.As both str1 and str2 points to same
memory location,they both point to the same object
"""

str1 = "Hello"
print("str1 is : ",str1)
print("ID of str1 is :",id(str1))

str2 = "World"
print("str2 is :",str2)
print("ID of str1 is :",id(str2))
str1 += str2
print("str1 after concatenation is: ",str1)
print("Id of str1 is :",id(str1))
str3 = str1
print("str3 = ",str3)
print("ID of str3 is :",id(str3))