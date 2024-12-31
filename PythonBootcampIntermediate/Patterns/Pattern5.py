"""

print the following pattern

1 1 1 1 1
* 2 2 2 2
* * 3 3 3
* * * 4 4
* * * * 5

observations:
first row is independent so we have to print it first
after that we need to first print stars => then to print the numbers
number of rows = no of columns

"""

for i in range(1,6):

    #work for current row

    #for spaces
    for csp in range(1,i):
        print("*",end=" ")

    #for numbers
    for j in range(1,7-i):
        print(j,end=" ")

    #prep for next row
    print() #prints new line after a complete row is printed
