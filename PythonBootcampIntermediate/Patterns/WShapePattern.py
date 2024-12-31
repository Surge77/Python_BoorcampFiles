"""
Print the following pattern

*     *     *
*   *   *   *
* *       * *
*           *

1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed
3.This pattern shall be divided into three parts first is the col 0 and 6 second is rising star line and third declining
line
4.For the third part which are the last two start we directly put the position of row and column
"""

i = 0
j = 3
for row in range(4):
    for col in range(7):
        if col==0 or col==6 or (col==4 and row==1) or (col==5 and row==2):
            print("*",end="")
        elif (row==i and col==j):
            print("*", end="")
            i = i + 1
            j = j - 1
        else:
            print(end=" ")
    print()