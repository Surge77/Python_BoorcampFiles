"""
Write a program to find whether the given number is an armstrong number

HInt: An armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the
number itself.For ex: 371 is an armstrong number since 3**3 + 7**3 + 1**3 = 371
"""


def is_armstrong(n):
    # Convert the number to a string to make it easier to work with the digits
    n_str = str(n)
    num_digits = len(n_str)

    # Calculate the sum of the digits each raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in n_str)

    # Check if the sum is equal to the original number
    return sum_of_digits == n


# Test the function with some examples
print(is_armstrong(371))  # Should print True
print(is_armstrong(123))  # Should print False


