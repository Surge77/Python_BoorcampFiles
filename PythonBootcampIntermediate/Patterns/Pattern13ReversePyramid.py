"""

Print the following pattern

    * * * * *
     * * * *
      * * *
       * *
        *


Observations:
1.Draw a grid around the pattern to understand how to print spaces and stars
2.we need to print spaces -> stars
3.with each row spaces get increased by 1 and stars decrease by 1
"""

num = int(input("Enter the number of rows: "))

# for i in range(0,num):
#
#     # work for current row
#     # printing spaces  csp -> count of spaces
#     for csp in range(0,i+1):
#         print(end=" ")
#
#     # printing stars
#     for j in range(0,num-i):
#         print("*",end=" ")
#
#     # prep for next row
#     print()

# another way of doing using step size

for i in range(num,0,-1):

    # printing current row
    # spaces
    for csp in range(0,num-i):
        print(end=" ")

    # stars
    for j in range(0,i):
        print("*",end=" ")

    print()

