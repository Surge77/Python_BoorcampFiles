"""
WAP to add two integers using a function
"""

def add(a, b):
    c = a + b
    return c

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

result = add(num1,num2)
print(f"Sum of {num1} and {num2} = {result}")

