"""

print the following pattern

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

"""

for i in range(1,6):
    #work for current row
    for j in range(1,i+1):
        print(i,end=" ") #till this loop is complete it will keep printing on same line because of end parameter
        #for printing the row number we just have to put i

    #prep for next row
    print() #prints new line after printing a full row