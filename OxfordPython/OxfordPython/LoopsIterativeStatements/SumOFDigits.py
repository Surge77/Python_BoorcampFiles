"""
WAP to enter a number and then calculate the sum of its digits

Programming tip: Placing a semi-colon after the while and for loop is not a syntax error.So it will not be reported by
the compiler. However it is considered to be a logical error as it changes the output of the program
"""

# Get the number from the user
num = int(input("Enter a number: "))

# Initialize the sum of digits to zero
sum_of_digits = 0

# Calculate the sum of the digits
while num > 0:
    # Get the last digit
    digit = num % 10

    # Add the digit to the sum
    sum_of_digits += digit

    # Remove the last digit from the number
    num = int(num // 10)

# Display the sum of digits
print("The sum of the digits of", num, "is", sum_of_digits)

