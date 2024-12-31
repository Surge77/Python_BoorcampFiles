"""

print the following pattern

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

observations:
we have to just print the numbers

"""

for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()