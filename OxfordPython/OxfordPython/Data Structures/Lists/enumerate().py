"""
WAP to illustrate the use of enumerate() to print an individual item and its index in the list

Enumerate(): This is used when you want to print both index as well an item in the list.The enumerate() function returns
an enumerate object which contains the index and value of all the items of the list as tuple
"""

num_list = [1,2,3,4,5]

for index,i in enumerate(num_list):
    print(f"{i} is at the index {index}")