"""
WAP to demonstrate the use of match() function

Regular expressions are a powerful tool for various kinds of string manipulation.These are basically a special text string
that is used for describing a search pattern to extract information from text such as code,files,log,spreadsheets or
even documents

Regular expressions are a domain specific language(DSL) that is present as a library in most of the modern programming
languages,besides python.A regular expression is a special sequence of characters that helps to match or find strings
in another string.In python regular expressions can be accessed using the re module which comes as a part of the
standard library.

Note:On success,match() function returns an object representing the match,else returns none
"""

import re

string = "She sells sea shells on the sea shore"
pattern1 = "sells"
if re.match(pattern1,string):
    print("match found")
else:
    print(pattern1,"is not present in the string")
pattern2 = "She"
if re.match(pattern2,string):
    print("MAtch found")
else:
    print(pattern2,"is not present in the string")

# In the above function sells is present in the string but still we got the output as match not found.This is because
# the re.match() function finds a match only at the beginning of the string.Since word sells is present in the middle of string