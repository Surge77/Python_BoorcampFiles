"""
WAP to demonstrate the use of {m,n} regular expression

tip: metacharacter '+' means {1,}
"""

import re

pattern = r"2{1,4}$"

if re.match(pattern,"2"):
    print("Match 2")
if re.match(pattern,"222"):
    print("Match 222")
if re.match(pattern,"22222"):
    print("Match 22222")   # does not match because only max 4 2's will match
