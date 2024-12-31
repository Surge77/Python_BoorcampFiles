"""
Program to compare two objects of user defined type
"""

class Book:

    def __init__(self):
        title = " "
        publisher = " "
        price = 0

    def set(self,title,publisher,price):
        self.title = title
        self.publisher = publisher
        self.price = price

    def display(self):
        print("title: ",self.title)
        print("publisher: ",self.publisher)
        print("price: ",self.price)

    def __gt__(self, other):
        if self.price > other.price:
            return True
        else:
            return False

b1 = Book()
b1.set("oop with cpp","Oxford publication",525)

b2 = Book()
b2.set("Let us c","BPB",345)

if b1>b2:
    print("This book has more knowledge: ")
    b1.display()


