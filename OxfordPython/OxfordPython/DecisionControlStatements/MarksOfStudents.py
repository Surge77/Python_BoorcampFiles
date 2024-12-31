"""
Write a program to enter the marks of a student in four subjects.Then calculate the total and average/aggregate and display the
grade obtained by the student.If the student scores an aggregate greater than 75%,then the grade is distinction.If
aggregate is 60>= and <75 then the grade is first division.If aggregate is 50>= and <60,then the grade is second division
If aggregate is 40>= and <50 then the grade is third division.Else the grade is fail
"""

marks1 = int(input("Enter the marks of Mathematics: "))
marks2 = int(input("Enter the marks of Science: "))
marks3 = int(input("Enter the marks of Social Science: "))
marks4 = int(input("Enter the marks of Computers: "))

total = marks1+marks2+marks3+marks4

average = float(total)/4

print(f"Total = {total}\t Aggregate = {average}")

if (average>=75):
    print("Distinction")
elif (average>=60 and average<75):
    print("First division")
elif (average>=50 and average<60):
    print("Second division")
elif (average>=40 and average<50):
    print("Third division")
else:
    print("Fail")

