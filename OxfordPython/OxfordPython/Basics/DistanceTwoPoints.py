"""
Write a program to calculate the distance between two points


"""

x1 = int(input("Enter the x coordinate of first point: "))
y1 = int(input("Enter the y coordinate of first point: "))
x2 = int(input("Enter the x coordinate of second point: "))
y2 = int(input("Enter the  y coordinate of second point: "))

distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("The distance is ",distance)
