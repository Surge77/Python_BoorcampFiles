"""
WAP to calculate GCD using recursive function

Note: recursive functions can become infinite if you don't specify the base case
"""

def GCD(x,y):
    rem = x%y
    if (rem==0):
        return y
    else:
        return GCD(y,rem)

n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

print("The GCD of two numbers is: ",GCD(n,m))