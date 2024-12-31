"""

Print the following pattern

*
*
*
*
*
*
* * * * *

Observations:
1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed

"""

for row in range(7):
    for col in range(5):
        if (col==0 or (row==6 and col>=0)):
            print("*",end="")
        else:
            print(end=" ")
    print()  # prints space after printing each row i.e adds new line