"""
Write a program to find the largest of two numbers

"""

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if(a>b):
    print(f"{a} is largest")
else:
    print(f"{b} is largest")

# another way of writing
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
if(a>b):
    large = a
else:
    large = b
print(f"Largest = {large}")