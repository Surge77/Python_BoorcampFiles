"""

Print the A shape pattern

      * * *
    *       *
    *       *
    * * * * *
    *       *
    *       *
    *       *

OR

    * * * * *
    *       *
    *       *
    * * * * *
    *       *
    *       *
    *       * if we want to print this pattern we just have to remove the row!=0 condition
Observations:
1.we need two nested for loops
2.Draw a grid to analyse the pattern
3.we need a if condition for printing the columns



"""

for row in range(7):
    for column in range(5):
        if ((column==0 or column==4) and (row!=0)) or ((row==0 or row==3) and (column>0 and column<4)):
            print("*",end="")
        else:
            print(end=" ") # the spaces in between stars is printed by this line
    print() # space after every row

print()


for row in range(7):
    for column in range(5):
        if ((column==0 or column==4)) or ((row==0 or row==3) and (column>0 and column<4)):
            print("*",end="")  # ****** prints without space
        else:
            print(end=" ") # the spaces in between stars is printed by this line
    print() # space after every row


print()
print()

# another method if we dont understand the end concept

str1 = ""
for row in range(7):
    for column in range(5):
        if ((column==0 or column==4) and (row!=0)) or ((row==0 or row==3) and (column>0 and column<4)):
            str1 = str1+"*"
        else:
            str1 = str1+" "
    print() # space after every row








