"""
Print the following patten

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

Floyd's triangle because the numbers are arranged in right-angled triangle shape

1.Draw a grid and analyse the rows and columns
2.here we take n input from user
3.Here we are printing the corresponding row number as the elements in the pattern
"""

n = int(input("Enter the number of rows: "))

for row in range(1,n+1):
    for col in range(1,row+1):  # here row+1 is excluded
        print(row,end=" ")
    print() # new line after a row is being printed