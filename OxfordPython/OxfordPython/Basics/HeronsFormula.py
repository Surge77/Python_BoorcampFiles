"""
Write a program to calculate area of triangle using herons formula

herons formula : area = sqrt(S*(S-a)*(S-b)*(S-c))


"""

a = float(input("Enter the first side of the triangle: "))
b = float(input("Enter the second side of the triangle: "))
c = float(input("Enter the third side of the triangle: "))

print(a,b,c)

S = (a+b+c)/2

area = (S*(S-a)*(S-b)*(S-c))**0.5 # the sqrt is written as 0.5th power

print("Area = " + str(area))

