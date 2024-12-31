"""

Write a program to perform two logical and two comparison operation on two input number
"""

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform comparison operations
is_equal = num1 == num2
is_not_equal = num1 != num2
is_greater = num1 > num2
is_less = num1 < num2

# Perform logical operations
is_same_sign = (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0)
is_opposite_sign = (num1 > 0 and num2 < 0) or (num1 < 0 and num2 > 0)
is_between_50_and_100 = 50 < num1 < 100 and 50 < num2 < 100

# Print results
print("Is num1 equal to num2?", is_equal)
print("Is num1 not equal to num2?", is_not_equal)
print("Is num1 greater than num2?", is_greater)
print("Is num1 less than num2?", is_less)
print("Do num1 and num2 have the same sign?", is_same_sign)
print("Do num1 and num2 have opposite signs?", is_opposite_sign)
print("Are both num1 and num2 between 50 and 100 (inclusive)?", is_between_50_and_100)