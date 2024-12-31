"""
WAP that emulates count() function
"""

def count_ch(s,c):
    count = 0
    for i in s:
        if i == c:
            count += 1
    return count

str = input("Enter a string: ")
ch = input("Enter the character to be searched: ")
cnt = count_ch(str,ch)

print(f"In {str} {ch} occurs {cnt} times")