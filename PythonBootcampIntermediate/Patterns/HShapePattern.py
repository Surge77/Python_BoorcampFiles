"""

Print the following pattern

*       *
*       *
*       *
* * * * *
*       *
*       *
*       *

observations:
1.Draw a grid to analyse rows and columns
2. there are 7 rows and 5 columns
3.We need two nested for loops
4.One for rows and other for columns
5.
"""

#my way of doing
# for row in range(7):
#     for col in range(5):
#         if (col==0 or col==4) or (row==3 and (col!=1 or col!=2 or col!=3)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

#another way of doing
for row in range(7):
    for col in range(5):
        if col==0 or col==4 or (row==3 and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()