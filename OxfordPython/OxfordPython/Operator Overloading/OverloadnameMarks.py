"""
Write a program that overloads the + operator on a class student that has attributes name and marks

"""

class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name,self.marks)

    def __add__(self, other):
        temp = Student(other.name,[])
        for i in range(len(self.marks)):
            temp.marks.append(self.marks[i] + other.marks[i])
        return temp

s1 = Student("Nikil", [87,54,74])
s2 = Student("Nikil", [78,98,78])

s1.display()
s2.display()

s3 = Student("",[])

s3 = s1 + s2
s3.display()