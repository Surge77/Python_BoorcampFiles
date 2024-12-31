"""
Write a python program to print unique values
from the list given below.
A=
[1,2,4,5,2,4,3,6,7,8,3,22,12,1,33,22,2,6,2,2,4,2,
2]
"""

A = [1,2,4,5,2,4,3,6,7,8,3,22,12,1,33,22,2,6,2,2,4,2,2]

unique_values = set(A) # a set does not have a duplicate element
# Here, the set() function is used to convert the list A into a set. This operation automatically removes duplicate
#elements from the list, leaving only the unique values in the set. The result is stored in a variable named unique_values.
print("Unique values in the list:")
for value in unique_values:
    print(value,end=" ")
print()

# other way of doing using function

def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

print(f"The list with unqiue values: {unique_list(A)}")




