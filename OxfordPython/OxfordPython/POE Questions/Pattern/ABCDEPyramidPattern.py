"""
Print the following pattern

A
A B
A B C
A B C D
A B C D E

"""

n = int(input("Enter number of row: "))
for row in range(1,n):
    for col in range(1,row+1):
        print(chr(64+col),end=" ")
    print()

