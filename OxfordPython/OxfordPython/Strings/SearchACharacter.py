"""
WAP that finds whether a given character is present in a string or not.In case it prints the index at which it is present
Do not use built in find function to search the character
"""

def find_char(s,c):
    index = 0
    while (index < len(s)):
        if s[index] == c:
            print(c,"found in string at index", index)
        else:
            pass
        index += 1
    print(c,"is not present in the string")

str = input("Enter the string: ")

ch = input("Enter the character to be searched: ")
print(find_char(str,ch))