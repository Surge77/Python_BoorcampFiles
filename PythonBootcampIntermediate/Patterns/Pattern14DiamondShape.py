"""

Print the following pattern

        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *
    * * * * *
     * * * *
      * * *
       * *
        *


Observations:
1.Draw a grid around the pattern to understand how to print spaces and stars
2.There are two for loops
3.First for loop to print the first half and the second for loop for printing the second half of loop
"""

num = int(input("Enter the number of rows: "))

for i in range(num):
    print(' '*(num-i-1)+'* '*(i+1))
for j in range(num-1,0,-1):
    print(' '*(num-j)+'* '*(j))





