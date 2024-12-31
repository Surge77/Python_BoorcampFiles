"""

print the following pattern

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

observation:
here i = j no of rows = no of columns
Each row represents the numbers from 1 to the row number.
The outer loop controls the number of rows, and the inner loop prints the numbers in each row.

"""


for i in range(1,6):
    #work for current row
    for j in range(1,i+1):
        print(j,end=" ") #till this loop is complete it will keep printing on same line because of end parameter

    #prep for next row
    print() #prints new line after printing a full row

