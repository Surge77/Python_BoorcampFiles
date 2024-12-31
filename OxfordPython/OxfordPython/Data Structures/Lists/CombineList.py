"""
WAP to combine and print elements of two list using list comprehension
"""

print([(x,y) for x in [10,20,30] for y in [31,10,40] if x!=y])