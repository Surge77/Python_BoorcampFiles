"""
WAP to demonstrate findall() function

The findall() function is used to search a string and returns a list of matches of the patten in the string.If no match
is found,then the returned list is empty.

matchList = re.findall(pattern,input_str,flags=0)

Note: The re.findall() function returns a list of all substrings that match a pattern
"""

import re

pattern = r"[a-zA-Z]+ \d"

matches = re.findall(pattern, "LXI 2013 , VXI 2015, VDI 20104, MAruti suzuki cars in india")

for match in matches:
    print(match,end=" ")

# In above code the regular expression = r"[a-zA-Z]+ \d+ ", finds all patterns that begin with one or more characters
# followed by a space and then followed by one or more digits