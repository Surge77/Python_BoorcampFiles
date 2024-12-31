"""
Print the following pattern

*       *
* *   * *
*   *   *
*       *
*       *
*       *
*       *

Observations:
1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed
3.We again divide this pattern in 4 parts first is col1 second is last column and
"""

for row in range(7):
    for col in range(7):
        if col == 0 or col==6 or (row==col and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==4):
            print("*",end="") # empty string for no space after each star
        else:
            print(end=" ") # space in each row

    print()  # new line