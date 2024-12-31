"""
WAP illustrating the modification of instance variable
"""

class Number:
    even = 0 # default value
    def check(self,num):
        if num%2==0:
            self.even = 1
    def Even_odd(self,num):
        self.check(num)
        if self.even == 1:
            print(num,"is even")
        else:
            print(num,"is odd")

n = Number()
n.Even_odd(26)