"""

Maximum of two numbers in python

"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

# simple method using conditionals
if (a > b):
    print(f"{a} is greatest")
elif (b > a):
    print(f"{b} is greatest")
elif (a == b):
    print(f"a and b are equal")
else:
    print("Enter a valid number")

# we can also use max() function which returns maximum of two or more numbers
# here we took 4 numbers to check if the function works for multiple numbers

max_value = max(a,b,c,d)
print(f"The maximum value is {max_value}")

# this is a one-liner ternary operator
max_valuee = a if a > b else b
print("The maximum value is ",max_valuee)



