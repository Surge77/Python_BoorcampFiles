"""
Metacharacters make regular expressions more powerful than normal string methods,They allow you to create regular
expressions to represent concepts like "one more repetition of a vowel"

Python allows users to specify metacharacters like (like +,?,.,*,$,(),[],{},|,\)

When we put the characters to be matches inside square brackets,we call it a character class.For ex: [aeiou] defines a
character class that has a vowel character

Other metacharacters like $ and . have no meaning within character classes.Moreover the metacharacters ^ have no meaning
unless it is the first character in the class

Metacharacters like *,+,? specify number of repetitions
* matches 0 or more occurrences of the regular expressions


WAP to check if the string has at least one vowel
"""

import re
pattern = r"[aeiou]"

if re.search(pattern,"clue"):
    print("Match clue")

if re.search(pattern,"bcdfg"):
    print("Match bcdfg")


