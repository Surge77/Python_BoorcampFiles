"""
Program to form highest possible 6 digit number from given six digit number as input
"""


def highest_possible_number(n):
    digits = list(str(n))
    digits.sort(reverse=True)
    return int(''.join(digits))

# Test the function
n = 123456
print(highest_possible_number(n))  # Output: 654321