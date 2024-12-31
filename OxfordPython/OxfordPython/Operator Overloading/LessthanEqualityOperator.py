"""
Write a program to compare two date objects
"""

class Date:

    def __init__(self):
        d = m = y = 0

    def get(self):
        self.d = int(input("Enter the day: "))
        self.m = int(input("Enter the month: "))
        self.y = int(input("Enter the year: "))

    def __eq__(self, other):
        Flag = False
        if self.m == other.m:
            if self.d == other.d:
                if self.y == other.y:
                    Flag = True
        return Flag

    def __lt__(self, other):
        Flag = False
        if self.d < other.d:
            if self.m < other.d:
                if self.y < other.y:
                    Flag = True
        return Flag



d1 = Date()
d1.get()
d2 = Date()
d2.get()
print("d1 == d2",d1 == d2)
print("d1 < d2",d1 < d2)