"""
WAP using for loop to calculate the factorial of a number
"""

num = int(input("Enter any number: "))

if (num==0):
    fact = 1

fact = 1

for i in range(1,num+1):
    fact = fact*i

print(f"The factorial of {num} is {fact}")