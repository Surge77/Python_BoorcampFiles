"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

n = int(input("Enter number of rows: "))

for row in range(1,n):
    for col in range(1,row+1):
        print(,end=" ")
    print()