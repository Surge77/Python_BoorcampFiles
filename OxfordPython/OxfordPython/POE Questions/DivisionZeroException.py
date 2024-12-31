"""
Write a python program to handle the division
by zero exception
"""

def safe_divide(dividend,divisor):
    # Use a try-except block to catch the ZeroDivisionError exception.
    try:
        # Divide the dividend by the divisor and return the result.
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        # If the divisor is zero, print an error message and return None.
        print('Error: Division by zero is not allowed.')
        return '' # We modify the safe_divide function to return an empty string ('') instead of None when the divisor is zero.
        # Note that returning an empty string may not be appropriate for all use cases.


numerator = int(input("Enter the first number: "))
denominator = int(input("Enter the second number: "))

print(safe_divide(numerator,denominator))