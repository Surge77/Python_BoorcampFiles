"""
Program to create a copy as well as the clone of the original list

If you want to modify and also keep a copy of the original list,then you should create a separate copy of the list
(not just the reference) This process is called cloning.The slice operation is used to clone a list
"""

list1 = [1,2,3,4,5,6,7,8,9,10]

list2 = list1  # copies a list using reference

print("List1 = ",list1)
print("List2 = ",list2)  # both lists point to the same list

list3 = list1[2:6]
print("List3 = ",list3) # list is a clone of list1