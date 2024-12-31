"""
WAP to demonstrate the metacharacter +
"""

import re

pattern = r"hi(de)+"

if re.search(pattern, "hidededede"):
    print("Match hidededede")

if re.search(pattern, "hi"):
    print("Match hi")  # at least one de required for match

