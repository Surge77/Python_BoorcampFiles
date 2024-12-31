"""

Write a python program to find largest of three numbers

"""

num1 = input("Enter first numbers: ")
num2 = input("Enter second numbers: ")
num3 = input("Enter third numbers: ")
#
# if num1 > num2 and num1 > num3:
#     print(f"{num1} is greatest")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is greatest")
# else:
#     print(f"{num3} is greatest")

# alternate method

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)