"""
Python program to exchange the values of two numbers without using a temporary variable

Addition: num1 = num1 + num2

At this point, num1 now holds the sum of the original values of num1 and num2 (a + b).
Subtraction: num2 = num1 - num2

Now, subtract the original value of num2 from the updated value of num1 ((a + b) - b).
This operation effectively assigns the original value of num1 to num2.
Subtraction: num1 = num1 - num2

Finally, subtract the updated value of num2 from the updated value of num1 ((a + b) - a). This operation effectively
assigns the original value of num2 to num1.
After these operations, the variables num1 and num2 have exchanged their original values without using a temporary variable.

"""

# Another way of doing this
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# print(f"Original values: num1 = {num1}, num2 = {num2}") # Prints the original values
#
# num1,num2 = num2,num1
#
# print(f"Original values: num1 = {num1}, num2 = {num2}")

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display the original values
print(f"Original values: num1 = {num1}, num2 = {num2}")

# Exchange values without using a temporary variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

# Display the values after exchange
print(f"After swapping: num1 = {num1}, num2 = {num2}")

