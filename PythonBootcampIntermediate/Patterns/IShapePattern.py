"""

Print the following pattern

* * * * *
    *
    *
    *
    *
* * * * *

observations:
1.Draw a grid to analyse the rows and columns
2.
"""
# my way of doing
# for row in range(7):
#     for col in range(5):
#         if col==2 or ((row==0 or row==6) and (row!=1 or row!=2 or row!=3 or row!=4)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()


# alternative way of doing
for row in range(7):
    for col in range(5):
        if col==2 or ((row==0 or row==6) and col!=2):
            print("*",end="")
        else:
            print(end=" ")
    print()