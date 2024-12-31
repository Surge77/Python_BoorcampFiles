"""

Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.

"""

# Computing area of a room

width = float(input("Enter width of room in m: "))
length = float(input("Enter length of room in m: "))

# Area of room = L*W

area = length * width

print(f"The area of room is {area} m")