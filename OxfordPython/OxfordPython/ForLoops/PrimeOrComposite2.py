"""
WAP to find a number is composite or prime

Explanation:

The all function returns True if all elements of the given iterable are true.
In this example, we check if number is not divisible by any number in the range [2, number).
If number is not divisible by any number in the range, then it is prime.
If number is divisible by any number in the range, then it is composite.

Note: This approach assumes that number is an integer greater than 1. If number is not in this range, then the result
may not be accurate.
"""

# Example usage
number = int(input("Enter a number: "))
classification = "prime" if all(number % i for i in range(2, number)) else "composite"
print(f"The number {number} is {classification}.")