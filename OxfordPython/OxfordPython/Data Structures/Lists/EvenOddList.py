"""
WAP that creates a list of 10 random integers.Then create two lists--odd list and even list that has all odd and even
values in the list respectively
"""

import random

num_list = []

for i in range(10):
    val = random.randint(1,100)
    num_list.append(val)

print("Original List : ",num_list)

odd_list = []
even_list = []

for i in range(len(num_list)):
    if (num_list[i] % 2 == 0 ):
        even_list.append(num_list[i])
    else:
        odd_list.append(num_list[i])

print("Even number list: ",even_list)
print("Odd number list: ",odd_list)