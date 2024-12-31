"""
print the following pattern

* * * * *
*
*
* * * * *
*
*
*
"""

for row in range(7):
    for col in range(5):
        # here we print star if row is 0,3,6 and at same time if col is 0 or greater than 0
        if col==0 or ((row==0 or row==3) and (col>0)):
            print("*",end="") # end="" means ***** prints star immediately without space
        else:
            print(end=" ") # the spaces are printed because of this condition
    print()