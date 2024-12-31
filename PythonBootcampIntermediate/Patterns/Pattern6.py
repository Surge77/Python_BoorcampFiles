"""

print the following pattern

1
2   3
4   5   6
7   8   9   10
11  12  13  14   15

observations:
always draw a grid to analyze the rows and columns
we have to just print the numbers
no of elements in each row = row number

"""

cnt = 1 #we used an external variable to print the incremented value every time in the row
for i in range(1,6):
    for j in range(1,i+1):
        print(cnt,end=" ")
        cnt += 1

    print()

