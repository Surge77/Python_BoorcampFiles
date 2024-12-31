"""
Print the following pattern

*           *
  *       *
    *   *
      *


1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed
3.We divide this pattern into 2 parts
3.We need two extra variables i and j for printing the 3 stars of right side


"""

i = 0
j = 6
for row in range(4):
    for col in range(7):
        if row==col:
            print("*",end="")
        elif (row==i and col==j):
            print("*",end="")
            i = i+1
            j = j-1
        else:
            print(end=" ")
    print()