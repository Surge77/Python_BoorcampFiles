"""
WAP using for loop to print all the numbers from m-n thereby classifying them as even or odd
"""

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

for i in range(m,n+1):
    if (i%2==0):
        print(i,"is even number")
    else:
        print(i,"is odd number")