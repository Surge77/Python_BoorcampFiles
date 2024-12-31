"""
Program to overload the + operator on a complex object
"""

class complex:
    def __init__(self):
        self.real = 0
        self.img = 0

    def setvalue(self,real,img):
        self.real = real
        self.img = img

    def __add__(self, other):
        Temp= complex()
        Temp.real = self.real + other.real
        Temp.img = self.img + other.img
        return Temp

    def display(self):
        print(f"( {self.img} + {self.real}i )")

c1 = complex()
c1.setvalue(1,2)
c2 = complex()
c2.setvalue(3,4)
c3 = complex()
c3 = c1 + c2

print("Result: ",end=" ")
c3.display()