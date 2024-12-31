"""
Write a python program and use function to
take two numbers and return the multiplication
of two numbers.
"""
# ------------------------------------------------------------------------------------------

# 1. Simple function
def multiply(num1, num2):
    return num1 * num2

result = multiply(3, 5)
print(result)

# ------------------------------------------------------------------------------------------

# 2. Using a function with default argument values
def multiply(num1=1, num2=1):
    return num1 * num2

result = multiply(3, 5)
print(result)  # Output: 15

result = multiply()
print(result)  # Output: 1 , this is due to the default values set

# ------------------------------------------------------------------------------------------

# 3. Using a lambda function
multiply = lambda num1, num2: num1 * num2

result = multiply(3, 5)
print(result)  # Output: 15

# ------------------------------------------------------------------------------------------------------
# 4. Using a function with variable-length arguments:
def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

result = multiply(3, 5)
print(result)  # Output: 15

result = multiply(3, 5, 7)
print(result)  # Output: 105

# ----------------------------------------------------------------------------------------------------------

# 5. Using a function with a list or tuple argument
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = [3, 5]
result = multiply(numbers)
print(result)  # Output: 15

numbers = (3, 5)
result = multiply(numbers)
print(result)  # Output: 15

# ------------------------------------------------------------------------------------------------------------------

# 6.Using a recursive function
def multiply(num1, num2):
    if num2 == 0:
        return 0
    elif num2 == 1:
        return num1
    else:
        return num1 + multiply(num1, num2-1)

result = multiply(3, 5)
print(result)  # Output: 15


