"""
Print the following pattern

*        *
  *    *
    *
  *   *
*       *

1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed

"""

i = 0
j = 4
for row in range(5):
    for col in range(5):
        if (row==i and col==j): # here sequence of condition matters if we write row==col first it produces different pattern
            print("*", end="")
            i = i  + 1
            j = j - 1
        elif row==col :
            print("*",end="")
        else:
            print(end=" ")
    print()