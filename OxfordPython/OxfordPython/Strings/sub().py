"""
WAP to demonstrate the use of sub() function

The sub() function in the re module can be used to search a pattern in the string and replace it with another pattern.

Syntax: re.sub(pattern, repl, string , max=0)

According to the syntax,the sub() function replaces all occurrences of the pattern in string with repl,substituting
occurrences unless any max value is provided.This method returns a modified string
"""

import re

string = "She sells sea shells on the sea shore"
pattern1 = "sea"
rep1 = "ocean"
new_string = re.sub(pattern1,rep1,string,1)
print(new_string)

# In above program, not that only one occurrence was replaces and not all because we had provided 1 as the value of max
