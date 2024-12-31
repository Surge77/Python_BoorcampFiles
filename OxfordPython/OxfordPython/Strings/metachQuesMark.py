"""
WAP to demonstrate use of metacharacter ?
"""

import re

pattern = r"hi(de)?"

if re.search(pattern, "hidededede"):
    print("Match hidededede")

if re.search(pattern, "hi"):
    print("Match hi")  # matches 0 or 1 occurrence