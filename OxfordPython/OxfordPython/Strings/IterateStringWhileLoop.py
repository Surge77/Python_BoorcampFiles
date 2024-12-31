"""
WAP to iterate through string by while loop
"""

str = "Welcome to python"

index = 0

while index < len(str):
    letter = str[index]
    print(letter,end=" ")
    index += 1