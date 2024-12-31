"""

Python program to read a number n and compute n+nn+nnn

"""

# A very basic way of doing this


# n = input("Enter a number: ")
#
# print(int(n) + int(n+n)+ int(n+n+n))

n = input("Enter a number: ")

# Calculate nn and nnn
nn = int(n * 2)
nnn = int(n * 3)

# Calculate the result
result = int(n) + nn + nnn

# Display the result
print(f"The result of {n} + {nn} + {nnn} is: {result}")