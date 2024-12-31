"""

print the following pattern

* * * * *
*
*
*
*
*
* * * * *

observations:
1.draw a grid to analyze the pattern
2. there are 7 rows and 5 columns according to zeroth indexing i.e range should be 7 and 5
3.We need two for loops to print the rows and columns

"""

for row in range(7):
    for col in range(5):
        if (((row==0 or row==6) and (col>0)) or (col==0)):
            print("*",end="")
        else:
            print(end=" ")
    print()

