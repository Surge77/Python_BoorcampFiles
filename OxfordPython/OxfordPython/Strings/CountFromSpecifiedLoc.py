"""
Modify the count program so that it starts counting from specified location
"""

def count_ch(s,c,beg = 0):
    count = 0
    index = beg
    while index < len(s):
        if s[index] == c:
            count += 1
        index += 1
    return count

str = input("Enter a string: ")
ch = input("Enter the character to be searched: ")
cnt = count_ch(str,ch)

print(f"In {str} {ch} occurs {cnt} times from beginning to end")

loc = int(input("From which position do you want to start counting: "))

cnt = count_ch(str,ch,loc)

print(f"In {str} {ch} occurs {cnt} times from position {loc} to end")


