"""

print the following pattern

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


"""

for i in range(1,6):
    for j in range(1,7-i):
        print(j,end=" ")
    print()
for i in range(2,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()