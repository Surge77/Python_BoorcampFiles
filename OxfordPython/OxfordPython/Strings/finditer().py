"""
WAP to demonstrate the use of finditer() function

The finditer() function is same as findall() function but instead of returning match objects it returns an iterator.
This iterator can be used to print the index of match of the given string

Note that start() function returns the starting index of the first match in the given string.Similarly we have end()
function which returns the ending index of the first match.Another method span() returns the starting and ending index
of the first match as a tuple

Note: The match objects returned by search(), match(), and findall() functions have start() and end() methods,that
returns the starting and ending index of first match
"""

import re

pattern = r"[a-zA-Z]+ \d"

matches = re.finditer(pattern, "LXI 2013 , VXI 2015, VDI 20104, MAruti suzuki cars witih us")

for match in matches:
    print("Match found at starting index: ",match.start())
    print("Match found at ending index: ", match.end())
    print("Match found at starting and ending index: ", match.span())
