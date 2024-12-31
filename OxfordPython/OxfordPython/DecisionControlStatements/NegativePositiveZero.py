"""
Program to test whether a number entered by the user is negative,positive or equal to zero

"""

num = int(input("Enter a number: "))

if (num==0):
    print("The value is equal to zero")
elif (num>0):
    print("The value is positive")
else:
    print("The number is negative")