"""

print the following pattern

1 2 3 4 5 5 4 3 2 1
1 2 3 4 * * 4 3 2 1
1 2 3 * * * * 3 2 1
1 2 * * * * * * 2 1
1 * * * * * * * * 1

observations:
we first need to print numbers => stars => numbers
first row is independent of any relation so we print it outside separately
with each row the stars are increased by 2
and with each row the number get decreased by 2

"""

for i in range(1,6):

    #work for current row
    for j in range(1,7-i):
        print(j,end=" ") #for printing this first half of row
    for cst in range(1,i):
        print("* *",end=" ") #for printing the stars in current row
    for j in range(6-i,0,-1):
        print(j,end=" ") #for printing the decreasing number in current row

    #prep for next row
    print() # prints new line after printing the current row