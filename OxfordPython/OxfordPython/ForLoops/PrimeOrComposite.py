"""
WAP to classify a given number as prime or composite

A prime number is a number that is greater than 1 and has only itself\
 and 1 as factors. A composite number is a number that has at least three factors
"""

number = int(input("Enter a number: "))

isComposite = 0

for i in range(2,number):
    if (number%i==0):
        isComposite = 1
        break

if (isComposite==1):
    print("The number is composite")
else:
    print("The number is prime")


