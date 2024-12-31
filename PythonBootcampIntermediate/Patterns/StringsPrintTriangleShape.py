"""
Printing the strings in right triangle shape

P
P Y
P Y T
P Y T H
P Y T H O
P Y T H O N


"""

string = input("Enter a string: ")
length = len(string)


for row in range(length):
    for col in range(row+1):
        print(string[col],end=" ")
    print()