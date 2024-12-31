"""
List is a versatile data type available in python.It is a sequence in which elements are written as a list of comma
separated values(items) between square brackets.The key feature of a list is that it can have elements that belong to
different data types

WAP to demonstrate slice operations used to access the elements in the list

seq = List[start:stop:step]
"""

num_list = [1,2,3,4,5,6,7,8,9,10]

print("num_list is: ",num_list)
print("The first element in the list is: ",num_list[0])
print("num_list[2:5] : ",num_list[2:5])
print("num_list[::2] : ",num_list[::2])
print("num_list[1::3] : ",num_list[1::3])