"""
A company decides to give bonus to all its employees on diwali.A 5% bonus on salary is given to the male workers and 10%
bonus on salary to the female workers.Write a program to enter the salary of the employees and sex of the employees.If
salary of the employees is less than 10k then the employee gets an extra 2% bonus on salary.Calculate the bonus that has
to be given to the employee and display the salary that the employee will get
"""

ch = input("Enter the sex of the employee (m or f): ")
sal = int(input("Enter the salary of employee: "))

if (ch == 'm'):
    bonus = 0.05*sal
else:
    bonus = 0.10*sal

amt_to_pay = bonus+sal
print("salary =  ",sal)
print("bonus = ",bonus)
print("*****************************")
print("Amount to be paid: ",amt_to_pay)