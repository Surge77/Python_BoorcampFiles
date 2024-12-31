"""
Create base class as student takes the name
and roll number of students as argument.
Create two methods inside class to display the
name of student and other method to display
roll number of student. Create two objects and
when + operator is used between two objects it
should return multiplication of roll numbers.
(Hint: Operator Overloading)
"""

class Student:

    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def name_display(self):
        print(f"The name of student is {self.name}")

    def roll_display(self):
        print(f"The roll no of student is {self.roll}")

    def __add__(self, other):
        return self.roll * other.roll

st1 = Student("tejas",4)
st2 = Student("rohan",23)

st1.name_display()
st1.roll_display()

st2.name_display()
st2.roll_display()

print(f"the product of roll numbers is {st1 + st2}")