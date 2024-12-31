"""
WAP to find the sum and mean of elements in a list
"""

num_list = [1,2,3,4,5,6,7,8,9,10]

sum = 0

for i in num_list:
    sum = sum + i

print("Sum of elements in the list: ",sum)
print("Average of elements in the list: ",float(sum/float(len(num_list))))