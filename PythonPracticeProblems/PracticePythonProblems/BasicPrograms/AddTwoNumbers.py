"""

To add two numbers

"""

def addNumbers(num1,num2):
    result = num1 + num2
    return result

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("The addition of numbers is: ", addNumbers(a,b))