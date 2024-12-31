"""
WAP to print the reverse of a number
"""

# Get the number from the user
num = int(input("Enter a number: "))

# Calculate the reverse of the number
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

# Display the reverse of the number
print("The reverse of", num, "is", reversed_num)