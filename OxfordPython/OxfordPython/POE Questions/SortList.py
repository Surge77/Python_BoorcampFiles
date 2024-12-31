"""
Write a python program to take the 6 input
numbers and store it in List and display it
ascending fashion
"""

num = input("Enter a six digit number: ")

list1 = []
for i in num:
    list1.append(i)

list1.sort()  # if we want to display in descending just write reverse=True in curly brackets

print(list1)

for j in list1:
    print(j,end="")
