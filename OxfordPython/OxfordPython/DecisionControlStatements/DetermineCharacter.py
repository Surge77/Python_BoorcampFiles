"""
Write a program to determine the character entered by the user
"""

char = input("Enter any key: ")

if (char.isalpha()): # 	alphabetic (A-Z, a-z)
    print("the user have entered a character")
if (char.isdigit()): # numeric (0-9)
    print("The user have entered a digit")
if (char.isspace()): 	# whitespace character: ' ', '\n', '\t', '\r'
    print("The user has enterd a white space character")
if (char.isalnum()): # alpha-numeric (A-Z, a-z, 0-9)
    print("The user have entered a ")

