"""
Print the following pattern

* * * * *
    *
    *
    *
    *
* * *

observations:
1.Draw a grid to analyse the rows and columns
2.we need two for loops for rows and columns

"""

for row in range(7):
    for col in range(5):
        if col==2 or ((row==0 or (row==6 and col!=3 and col!=4)) and col!=2):
            print("*",end="")
        else:
            print(end=" ")
    print()