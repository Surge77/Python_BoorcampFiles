"""
Print the following pattern

* * * * *
*
*
* * * * *
*
*
* * * * *

observations:
1.Draw a grid to analyse rows and columns
2.we need two nested for loops
3.One for row and other for columns
4.We are using if else conditional statements so that we can print stars as well as spaces
5.we are going to use logical and , logical or operator
"""

# for row in range(7):
#     for col in range(5):
#         # here we print star if row is 0,3,6 and at same time if col is 0 or greater than 0
#         if (((row==0 or row==6 or row==3) and (col>0)) or (col==0)):
#             print("*",end="")
#         else:
#             print(end=" ")
#     print()

#another way of representing the if else logic
for row in range(7):
    for col in range(5):
        # here we print star if row is 0,3,6 and at same time if col is 0 or greater than 0
        if col==0 or ((row==0 or row==3 or row==6) and (col>0)):
            print("*",end="") # end="" means ***** prints star immediately without space
        else:
            print(end=" ")
    print()

