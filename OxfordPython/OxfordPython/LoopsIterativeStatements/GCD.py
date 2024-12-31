"""
WAP to calculate the GCD of two numbers
"""

# Get the two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD using the Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

gcd_value = gcd(num1, num2)

# Display the GCD
print("The GCD of", num1, "and", num2, "is", gcd_value)