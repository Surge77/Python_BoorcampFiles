"""

Print the following pattern

    *
   * *
  * * *
 * * * *

 Observations:
1.Draw a grid around the pattern to understand how to print spaces and stars
2.We need to print spaces then stars
3.with every row the spaces get decreased by one and the stars increase by 1


"""
num = int(input("Enter the number of rows: "))


for i in range(0,num):

    # work for current row
    # spaces printing
    for csp in range(0,num-i-1):
        print(end=" ")

    # printing stars
    for j in range(0,i+1):
        print("*",end=" ")

    # prep for next row
    print()

# ANOTHER way of doing it
def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'*'*(2*i+1))

pyramid(num)

