class Book:

    def __init__(self):
        title = ""
        publication = ""
        price = 0

    def set(self,title,publication,price):
        self.title = title
        self.publication = publication
        self.price = price

    def dispay(self):
        print("title: ",self.title)
        print("publication: ",self.publication)
        print("price: ",self.price)

    def __gt__(self, other):
        if self.price > other.price:
            return True
        else:
            return False

b2 = Book()
b2.set("oop with cpp","Oxford publication",525)

b1 = Book()
b1.set("Let us c","BPB",345)

if b1>b2:
    print("This book has more knowledge: ")
    b1.display()