"""
Write a program to calculate tax given the following conditions

If income is less than 1,50,000 than no tax
If taxable income is 1,50,001 - 300000 then charge is 10%tax
If taxable income is 3,00,001 - 5,00,000 then charge 20% tax
If taxable income is above 5,00,001 then charge 30% tax
"""

min1 = 150001
max1 = 300000
rate1 = 0.10
min2 = 300001
max2 = 500000
rate2 = 0.20
min3 = 500000
rate3 = 0.30

income = int(input("Enter your income: "))

taxable_income = income - 150000

if (taxable_income<=0):
    print("No tax")
elif (taxable_income>=min1 and taxable_income<max1):
    tax = (taxable_income - min1) * rate1
elif (taxable_income>=min2 and taxable_income<max2):
    tax = (taxable_income - min2) * rate2
else:
    tax = (taxable_income - min3) * rate3

print("Tax = ",tax)