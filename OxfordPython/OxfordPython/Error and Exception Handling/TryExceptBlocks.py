"""
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception
 handling deals with these events to avoid the program or system crashing, and without this process, exceptions would
 disrupt the normal operation of a program.
"""

import DecisionControlStatements


try:
    age = int(input("Enter age"))
    income = 20000
    risk = income/age
    print(risk)
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError: # these are the type of errors which cause program to crash
    print("Invalid value")