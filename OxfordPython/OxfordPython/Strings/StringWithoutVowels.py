"""
WAP that accepts a string from user and redisplay the same string after removing vowels from it
"""

def rem_vowels(s):
    new_str = ""
    for i in s:
        if i in "aeiouAEIOU":
            pass
        else:
            new_str += i
    print("the string without vowels is: ",new_str)

str = input("Enter a string: ")
rem_vowels(str)