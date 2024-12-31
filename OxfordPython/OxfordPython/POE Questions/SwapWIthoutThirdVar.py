"""
Write a Python program to swap the values of
two numbers without using a temporary
variable
"""

# Get input from the user
num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

# Swap the values of num1 and num2
num1, num2 = num2, num1

# Print the swapped values
print("The swapped values are: ", num1, "and", num2)