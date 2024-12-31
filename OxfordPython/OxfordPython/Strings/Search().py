"""
WAP to demonstrate the use of search() function

The search() function searches for a pattern anywhere in the string.
The syntax is similar to match() the function searches for first occurrence of pattern within a string with optional
flags.If the search is successful a match object is returned and None otherwise

The re.search() finds a match of a pattern anywhere in the string
"""

import re

string = "She sells sea shells on the sea shore"
pattern1 = "sells"
if re.search(pattern1,string):
    print("match found")
else:
    print(pattern1,"is not present in the string")
