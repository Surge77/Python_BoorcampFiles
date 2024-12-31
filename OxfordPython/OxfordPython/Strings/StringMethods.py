"""
WAP that uses several string methods (upper,lower,split,join,count,replace and find) on string object
"""

str = "Welcome to the world of python"


print("Uppercase - ",str.upper())
print("Lowercase - ",str.lower())
print("Split - ",str.split())
print("Join - ",'-'.join(str.split()))
print("Count of o - ",str.count('o'))
print("Find of - ",str.find("of"))