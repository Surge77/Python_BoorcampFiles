"""
Print the following pattern

* * * * *
*       *
*       *
* * * * *
*   *
*     *
*       *

or

* * * *
*       *
*       *
* * * *
*       *
*       *
*       *

1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed


"""

for row in range(7):
    for col in range(5):
        if col == 0 or (col == 4 and (row == 1 or row == 2)) or ((row == 0 or row == 3) and (col > 0 and col < 4)) or ((row>3 and row<7) and col>3):
            print("*",end="")
        else:
            print(end=" ")
    print()