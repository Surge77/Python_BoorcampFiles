"""
WAP to demonstrate nested lists\

Nested list means a list within another list.
"""

list1 = [1, 'a', "abc", [1,2,4],8.9]

i = 0

while i<(len(list1)):
    print("List[",i,"] = ",list1[i])
    i += 1
