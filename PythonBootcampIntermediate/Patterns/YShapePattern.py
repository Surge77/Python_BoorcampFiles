"""
Print the following pattern

*       *
  *   *
    *
    *
    *

1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed
3.Here we divide the pattern again in three parts

"""

for row in range(5):
    for col in range(5):
        if (col==2 and row>1) or (row==col and row<3) or (row==0 and col==4 )or (row==1 and col==3):
            print("*", end="")
        else:
            print(end=" ")
    print()