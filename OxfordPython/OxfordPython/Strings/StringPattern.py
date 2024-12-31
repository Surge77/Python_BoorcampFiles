"""
Print the following pattern

A
AB
ABC
ABCD
ABCDE

The ord() function returns the ASCII code of the characters and the chr() function returns character represented by a
ASCII number
"""

for i in range(1,7):
    ch = 'A'
    print()
    for j in range(1,i+1):
        print(ch,end=' ')
        ch = chr(ord(ch)+1)
