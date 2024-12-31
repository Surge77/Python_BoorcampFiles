"""
Print the following pattern

* * * * *
    *
    *
    *
    *
    *
    *

1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed
"""

for row in range(7):
    for col in range(5):
        if row==0 or col==2:
            print("*",end="")
        else:
            print(end=" ")
    print()