"""

print the following pattern

* * * * *
*
*
*     * * *
*       *
*       *
* * * * *

observations:
1.draw a grid to analyse the rows and columns
2.we need stars and spaces in a particular pattern so we use if else conditional statement
"""
#
# for row in range(7):
#     for col in range(6):
#         if col==0 or (col==4 and (row!=1 and row!=2)) or( (row==0 or row==6) and (col>0 and col<4)) or ((row==3 )and (col!=1 and col!=2)):
#             print("*", end="")
#         else:
#             print(end=" ")
#     print()


for row in range(7):
    for col in range(6): # the only difference here is the last condition where the col condition is specified
        if col==0 or (col==4 and (row!=1 and row!=2)) or( (row==0 or row==6) and (col>0 and col<4)) or ((row==3 ) and (col==3 or col==5)):
            print("*", end="")  # end="" means ***** prints star immediately without space
        else:
            print(end=" ")  # the spaces are printed because of this condition
    print()