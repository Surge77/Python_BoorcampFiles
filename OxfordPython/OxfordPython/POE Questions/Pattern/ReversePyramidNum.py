"""
Print the following pattern

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

observations:
1.Draw a grid and analyse the following rows and columns
2.we need to use the step size in order to print the pattern
3.we keep reducing the number of columns as we go down the patttern
4.for each row we need the corresponding row number of columns i.e for row 5 we need 5 columns and for row 4 need 4 cols
"""

n = int(input("Enter number of rows: "))

for row in range(n,0,-1): # for such reducing patterns we need to use step size
    for col in range(1,row+1):
        print(col,end=" ")
    print()
