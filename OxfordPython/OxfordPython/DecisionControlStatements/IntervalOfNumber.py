"""
program that prompts the user to enter a number and then prints the interval
"""

num = int(input("Enter a number from 0-30: "))

if (num>0 and num<10):
    print("It is in the range 0-10")
elif (num>10 and num<20):
    print("It is in the range 10-20")
elif (num>20 and num<30):
    print("It is in the range 20-30")
else:
    print("It is more than 30 or less than 0")