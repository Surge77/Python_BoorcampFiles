"""
print the following pattern

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

observations:
The outer loop controls the number of rows, and the inner loop prints the numbers in each row.


"""

for i in range(1,6):

    #work for current row
    for j in range(1,7-i): #value of i changes with every iteration
        print(j,end=" ")

    #prep for next row
    print()