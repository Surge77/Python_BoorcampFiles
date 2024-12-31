"""
WAP to swap two numbers

"""

def swap(a,b):
    a,b = b,a
    print("After swapping: ")
    print("Value of a: ",a)
    print("Value of b: ",b)

a = input("Enter the first number: ")
b = input("Enter the second number: ")

print("Before swap: ")
print("Value of a: ",a)
print("Value of b: ",b)
swap(a,b)
