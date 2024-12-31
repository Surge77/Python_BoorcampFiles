"""
WAP to compute P(n,r)
"""

def fact(n):
    f = 1
    if (n==0 or n==1):
        return 1
    else:
        for i in range(1,int(n+1)):
            f = f*i
    return f

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
result = float(fact(n)/float(fact(r)))
print(f"P ( {n} / {r} ) = {result}")