"""
WAP to remove all duplicates from a list
"""

num_list = [1,2,3,4,5,6,7,6,5,4]
print("Original list is: ",num_list)

i = 0

while i<len(num_list):
    num = num_list[i]
    for j in range(i+1,len(num_list)):
        val = num_list[j]
        if val==num:
            num_list.pop(j)
    i += 1

print("List after removing duplicates: ",num_list)
