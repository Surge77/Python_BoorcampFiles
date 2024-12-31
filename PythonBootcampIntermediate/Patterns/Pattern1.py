"""

print the following pattern

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

"""

for i in range(1,6):
    #work for current row
    for j in range(1,6):
        print(j,end=" ")

        #prep for next row
    print() # after printing a whole row a new line is printed