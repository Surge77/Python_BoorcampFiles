"""
Print the following pattern

1
2 3
4 5 6
7 8 9 10

1.Draw a grid and analyse the rows and columns
2.here we take n input from user
"""

n = int(input("Enter the number of rows: "))

count = 1
for row in range(1,n+1):
    for col in range(1,row+1):  # here row+1 is excluded
        print(count,end=" ")
        count += 1
    print() # new line after a row is being printed