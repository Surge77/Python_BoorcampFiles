"""

print the following pattern

        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

observations:
here we need to first print spaces => then print numbers

"""
num = int(input("Enter the number of rows: "))
for i in range(1,num):

    #for printing spaces
    for csp in range(1,num-i):  #csp => count of spaces
        print(" ",end=" ")

    #for printing numbers
    for cn in range(1,i+1): #cn => count of numbers
        print(cn,end=" ") 

     #prep for next row
    print() #prints new row after printing a fulll row


# another way of printing same pattern with stars
def pyramid(rows):
    for i in range(rows):
        print(' '*(rows-i-1)+'*'*(i+1))

pyramid(num)
