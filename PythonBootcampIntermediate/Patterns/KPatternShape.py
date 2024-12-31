"""
Print the following pattern

*       *
*     *
*   *
* *
*   *
*     *
*       *

observations:
1.Draw a grid to analyse the rows and columns
2.We need two for loops for rows and columns
3.We divide this pattern into three parts
4.First is the first column and second is the inclined 4 upper stars and third is the lower 3 stars
5.We also need two extra variables two print the inclined 4 upper stars
6.In third part the logic or pattern observed is that when row == col+2 then star should be printed
7.In second part we used i and j and incremented and decremented according to the pattern
"""

i = 0
j = 4
for row in range(7):
    for col in range(5):
        if col==0 or (row==col+2 and col>1):
            print("*",end="")
        elif ((row==i and col==j)and col>0):
            print("*", end="")
            i = i+1
            j = j-1
        else:
            print(end=" ")
    print()  # to print space after each row is printed