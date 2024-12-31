"""
Write a program to form highest possible 6 digit number from given 6 digit number as input
"""

def highest_possible_number(n):
    digits = list(str(n))
    digits.sort(reverse=True)
    return int(''.join(digits))

# Test the function
n = input("Enter a six digit number: ")
print(highest_possible_number(n))  # Output: 654321