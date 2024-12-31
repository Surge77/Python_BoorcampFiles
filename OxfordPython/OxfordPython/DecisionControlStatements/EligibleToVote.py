"""

Write a program to determine whether a person is eligible to vote if not display how many years are left to be eligible
"""

age = int(input("Enter you age: "))

if (age >= 18):
    print("You are eligible to vote! ")
else:
    yrs = 18 - age
    print(f"You have to wait for another {yrs} years to be eligible to vote")
