"""
Print the following pattern

* * * * *
      *
    *
  *
* * * * *

1.Need two nested for loop for printing row and column
2.Draw a grid and analyse the row and columns where the star needs to be printed

"""
i = 1
j = 4
for row in range(0,6):
    for col in range(0,6):
        if row==5 or row==0:
            print("*",end="")
        elif row==i and col==j:
            print("*",end="")
            i = i + 1
            j = j - 1
        else:
            print(end=" ")
    print()