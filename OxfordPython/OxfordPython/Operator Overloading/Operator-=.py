"""
Write a program to overload the -= operator to subtract two Distances objects


"""

class Distance:

    def __init__(self):
        self.km = 0
        self.m = 0

    def set(self,km,m):
        self.km = km
        self.m = m

    def __isub__(self, other):
        self.m = self.m - other.m
        if self.m < 0:
            self.m += 1000
            self.km -= 1
        self.km = self.km - other.km
        return self

    def convert_to_meters(self):
        return (self.km*1000 + self.m)

    def display(self):
        print(f"{self.km} kms {self.m} mtrs")

d1 = Distance()
d1.set(21,70)
d2 = Distance()
d2.set(18,123)

d1 -= d2
print("d1 - d2: ",end=""),
d1.display(),
print(f"that is {d1.convert_to_meters()}")




