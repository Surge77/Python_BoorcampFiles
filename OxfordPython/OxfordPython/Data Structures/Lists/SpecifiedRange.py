"""
WAP to create a list of numbers in the specified range in particular steps.Reverse the list and print its values
"""


num_list = []

m = int(input("Enter the starting range: "))
n = int(input("Enter the ending of the range: "))
o = int(input("Enter the steps in the range: "))

for i in range(m,n,o):
    num_list.append(i)

print("Original list : ",num_list)
num_list.reverse()
print("Reversed List is: ",num_list)