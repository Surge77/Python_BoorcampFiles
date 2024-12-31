"""
WAP to calc GCD of two numbers
"""

# Get the two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if (num1>num2):
    dividend = num1
    divisor = num2
else:
    dividend = num2
    divisor = num1

while(divisor!=0):
    remainder = dividend%divisor
    dividend = divisor
    divisor = remainder
print(f"GCD of {num1} and {num2} is {dividend}")