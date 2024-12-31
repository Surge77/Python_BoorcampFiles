"""

Write a program to take input from the user and then check whether it is a number or a character.If it is a character,
determine whether it is in uppercase or lowercase
"""
ch = input("Enter the character: ")

if (ch>="A" and ch<="Z"):
    print("It is an uppercase Alphabet")
elif (ch>="a" and ch<="z"):
    print("It is a lowercase alphabet")
elif (ch>='0' and ch<='9'):
    print("It is a number")