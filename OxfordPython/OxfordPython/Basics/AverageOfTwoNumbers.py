"""
Write a program to calculate the average of two numbers Print their deviation

"""

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

avg =( num1+num2)/2

dev1 = num1 - avg
dev2 = num2 - avg

print("Average = ",avg)
print("Deviation of first num: ",dev1)
print("Deviation of second num: ",dev2)

