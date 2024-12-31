"""
Print the following pattern


*           *
* *         *
*   *       *
*     *     *
*       *   *
*         * *
*           *

1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed
3.
"""

for row in range(7):
    for col in range(7):
        if col==0 or col==6 or (row==col and col>0 and col<6):
            print("*",end="")
        else:
            print(end=" ") # for space between stars
    print()  # for new line