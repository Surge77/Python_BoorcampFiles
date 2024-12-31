"""
Write a program to calculate the roots of quadratic equation
"""

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

D = (b*b)-(4*a*c)
deno = 2*a

if(D>0):
    print("Real roots")
    root1 = (-b + D**0.5)/deno
    root2 = (-b - D**0.5)/deno
    print("Root1 = ",root1,"\tRoot2 = ",root2)
elif (D==0):
    print("Equal roots")
    root1 = -b/deno
    print("Root1 and Root2 = ",root1)
else:
    print("Imaginary roots")