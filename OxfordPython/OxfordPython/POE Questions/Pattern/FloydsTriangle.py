"""
Print the following patten

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Floyd's triangle because the numbers are arranged in right angled triangle shape

1.Draw a grid and analyse the rows and columns
2.here we take n input from user
"""

n = int(input("Enter the number of rows: "))

for row in range(1,n+1):
    for col in range(1,row+1):  # here row+1 is excluded
        print(col,end=" ")
    print() # new line after a row is being printed
