"""
WAP that has a list of both positive and negative numbers.Create another list using filter() that has only positive
values
"""

def is_positive(x):
    if x>=0:
        return x

num_list = [10,20,30,-20,-40,50,-60,70,-80,90,-100]

new_list = []

new_list = list(filter(is_positive,num_list))

print("Positive value list is: ",new_list)