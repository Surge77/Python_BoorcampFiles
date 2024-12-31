"""
print the following number pyramid pattern

        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

observations:
1.Draw a grid to analyse the rows and columns
2.Here we need to print spaces first then numbers


"""

n = int(input("Enter the number of rows: "))

for row in range(1,n):
    for csp in range(1,n-row): # count of spaces
        print(" ",end=" ")
    for col in range(1,row+1): # for printing number
        print(col,end=" ")
    print()
