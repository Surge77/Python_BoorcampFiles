"""
Write a program to enter any character.If the entered character is in lowercase then convert it into uppercase and if it
is an uppercase character,then convert it into lowercase

"""

ch = input("Enter any charcter: ")

if (ch >= 'A' and ch <= 'Z'):
    ch = ch.lower()
    print(f"The entered character was in uppercase. In lowercase it is {ch}")
else:
    ch = ch.upper()
    print(f"The entered character was in lowercase.In uppercase it is {ch}")