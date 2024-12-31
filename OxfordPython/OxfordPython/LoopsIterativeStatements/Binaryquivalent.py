"""
Write a program to enter a decimal number.Calculate and display the binary equivalent of this number
"""

# Get the decimal number from the user
decimal_num = int(input("Enter a decimal number: "))

# Convert the decimal number to binary
binary_num = bin(decimal_num)[2:] # [2:] syntax, it means that you want to extract all the characters in the string starting from the index 2 up to the end of the string.

# Display the binary equivalent
print("The binary equivalent of", decimal_num, "is", binary_num)