"""
Print the following pattern

  * * *
*       *
*       *
*       *
*       *
  * * *

1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed

"""

for row in range(7):
    for col in range(5):
        if ((col==0 or col==4 ) and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()