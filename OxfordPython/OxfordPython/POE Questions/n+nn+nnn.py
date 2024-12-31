"""
Write a Python program to read a number n
and compute n+nn+nnn and display the result

This just concatenates the numbers and adds them and prints the result
"""

# Get input from the user
n = int(input("Please enter a number: "))

# Compute n + nn + nnn
nn = n * 10 + n
nnn = n * 100 + nn
result = n + nn + nnn

# Print the result
print("The result is: ", result)


# second way
result = n + n * 11 + n * 111

# Print the result
print("The result is: ", result)

# third way of printing
print(int(n) + int(nn) + int(nnn))

print(int(nn)) # the two numbers just get joined