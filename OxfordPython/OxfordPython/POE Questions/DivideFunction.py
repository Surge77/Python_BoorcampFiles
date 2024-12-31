"""
Write a python program and use function to take two numbers and return the division of two numbers.
"""

# 1. using a simple function

def divide(num1, num2):
    return num1 / num2

result = divide(158, 29)
print(result)  # Output: 5.448275862068965

# 2. Using keyword arguments

def divide(**numbers):
    result = numbers['num1']
    divisor = numbers['num2']
    return result / divisor

result = divide(num1=158, num2=29)
print(result)  # Output: 5.448275862068965

result = divide(num1=158, num2=29, num3=2)
print(result)  # Output: 5.448275862068965